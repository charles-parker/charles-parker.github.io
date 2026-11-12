* 4-27-2026 - Nick is working through the file -- adding diagnostics etc;
* Some time before 4-27-2026 - Charles created;

proc printto;
run;

* Assign library;
* Nick's libraries
* ----------------;
%let workinglibpath = Y:\data\raw\tracker-2022-v1;
libname trk2022 "&workinglibpath";
libname inlib  "Y:\data\raw\data_using" access = readonly;
libname outlib "Y:\data\clean";
libname worklib "Y:\data\worklib";
* Charles' libraries
* ------------
* libname inlib  "C:\Users\charl\OneDrive\Documents\bsta_535\hrs-analyses\data\raw\data_using" access = readonly;
* libname outlib "C:\Users\charl\OneDrive\Documents\bsta_535\hrs-analyses\data\clean";
* libname worklib "C:\Users\charl\OneDrive\Documents\bsta_535\hrs-analyses\data\worklib";


* have to load in the sas format for the rand dataset;
proc format cntlin = inlib.Sasfmts
	lib = work;
run;

* load in rand dataset;
data worklib.rand;
	set inlib.randhrs1992_2022v1;
run;

data worklib.rand;
	retain HHIDPN_chr;
	set worklib.rand;
	HHIDPN_chr = put(HHIDPN, best12. -L);
	drop HHIDPN;
run;

data worklib.rand;
	set worklib.rand (rename = (HHIDPN_chr = HHIDPN));
run;

* add tracker file to rand dataset by pt id, need to first combine household id + pt id to match rand;
data worklib.tracker;
	* For Nick;
	set trk2022.trk2022tr_r;
	* For Charles;
	* -----------;
	*set inlib.trk2022tr_r;
	HHIDPN = cats(HHID, PN);
run;

* Diagnostic: PROC COMPARE on HHIDPN;
* We drop ~1k cases, oh well.;
proc sort data=worklib.rand;
   by HHIDPN;
run;
proc sort data=worklib.tracker ;
   by HHIDPN;
run;
proc compare base=worklib.rand compare=worklib.tracker nosummary;
   var HHIDPN;
   with HHIDPN;
   title 'RAND and Tracker datasets -- do HHIDPN valuds fully match?';
run;


proc sql;
	create table worklib.combined as
	select a.*, 
		   b.EXDEATHMO,
		   b.EXDEATHYR,
	/* For diagnostic purposes, merge in weighting/cohort vars from teh trackign table too; */
		   b.SECU,
		   b.STRATUM,
		   b.WTCOHORT,
		   b.HHBASEWT,
 	/* As well as birth date */
		   b.BIRTHMO,
		   b.BIRTHYR	
	from worklib.rand as a
	left join worklib.tracker as b
	on a.HHIDPN = b.HHIDPN;
quit;

* save the combined dataset in outlib folder;
data outlib.combined_rand_v1;
	set worklib.combined;
run;
