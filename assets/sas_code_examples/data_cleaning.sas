* 4-27-2026 - Nick adds in month-year retirement answers;
* Some time before 4-27-2026 - Charles created;

* Assign library;
* Nick's libraries
* ----------------;
libname inlib  "Y:\data\raw\data_using" access = readonly;
%let outlib = Y:\data\clean;
libname outlib "&outlib";
libname worklib "Y:\data\raw\data_using";
* Charles' libraries
* ------------
* libname inlib  "C:\Users\charl\OneDrive\Documents\bsta_535\hrs-analyses\data\raw\data_using" access = readonly;
* libname outlib "C:\Users\charl\OneDrive\Documents\bsta_535\hrs-analyses\data\clean";
* %let outlib = C:\Users\charl\OneDrive\Documents\bsta_535\hrs-analyses\data\clean;
* libname worklib "C:\Users\charl\OneDrive\Documents\bsta_535\hrs-analyses\work"

* have to load in the sas format for the rand dataset -- let's
* do so within both our working and output libraries;
proc format cntlin = inlib.Sasfmts
	lib = worklib;
run;
proc format cntlin = inlib.Sasfmts
	lib = outlib;
run;


data worklib.rand_respondents;
	set outlib.combined_rand_v1; /* Created in 'combine_rand_tracker.sas' */
	keep HHIDPN
		R3:
		R4:
		R5:
		R6:
		R7:
		R8:
		R9:
		R10:
		R11:
		R12:
		R13:
		R14:
		R15:
		RARACEM
		RAGENDER
		RAHISPAN
		RAEDUC
		EXDEATHMO
		EXDEATHYR
		RADDATE
		H:
		INW3-INW15
		RAEHSAMP
		RAESTRAT
		  /* ...Tracker birth date... */
		BIRTHMO
		BIRTHYR
		  /* ...and longitudinal dataset birth date... */
		RABDATE
;
run;

proc contents data = worklib.rand_respondents varnum;
run;

%macro waves(var);
%do i = 3 %to 15;
	R&i.&var
%end;
%mend;

%macro hvar(var);
%do i = 3 %to 15;
	H&i.&var
%end;
%mend;

data worklib.rand_sort_columns;
	retain HHIDPN
				%waves(LGMUSA) /*physical functional domain model (FDM)*/
				%waves(MOBILA) /* physical FDM*/ 
				%waves(BMI) /* nutritive FDM*/ 
				%waves(WEIGHT) /* nutritive FDM*/
				%waves(COG27) /* cognitive FDM*/ 
				%waves(PRMEM) /* proxy report for cognitive FDM*/
				%waves(EYERT) /*sensory FDM*/
				%waves(EARRT) /*sensory FDM*/
				%waves(CONDE) /* Disease Frailty Index*/
                %waves(ADL6A) /* functional limitation FI*/
                %waves(IADL5A) /*instrumental activities FI*/
				%waves(CESD) /* Mental Impairment FI*/
                %waves(LBRF) /* retirement status*/
				%waves(AGEY_B) /*age at beginning of interview for each wave*/
				RARACEM /* race masked*/
				RAGENDER /* gender*/
				RAHISPAN /* hispanic (ethnicity) */
				%waves(MSTAT) /* Spouse*/
				RAEDUC /* general education level*/
				%hvar(ATOTB) /* total wealth*/
				EXDEATHMO /*month of death*/
				EXDEATHYR /* year of death*/
				%waves(IWEND) /*interview end date*/
				%waves(WTRESP) /* per-wave respondent weight */
				RADDATE
				INW3-INW15
				%waves(IWSTAT)
				%waves(NHMLIV)
				%hvar(CPL)
				RAEHSAMP
				RAESTRAT
				/* Nick here - adding some alternate month-year retirement data too */
				%waves(SAYRET)
				%waves(RETMON)
				%waves(RETYR)
				%waves(RETDTWV) /* Indicates original wave in which these particualr mo/years reported */
				  /* ...Tracker birth date... */
				BIRTHMO
				BIRTHYR
				  /* ...and longitudinal dataset birth date... */
				RABDATE
	;
	set worklib.rand_respondents;
run;

proc contents data = worklib.rand_sort_columns varnum;
run;

/* This previously created a new dataset 'rand_filter'; let's just update an old one in place */
data worklib.rand_sort_columns;
	set worklib.rand_sort_columns;
		keep  HHIDPN
				R3LGMUSA--R15LGMUSA /*physical functional domain model (FDM)*/
				R3MOBILA--R15MOBILA /* physical FDM*/ 
				R3BMI--R15BMI /* nutritive FDM*/ 
				R3WEIGHT--R15WEIGHT /* nutritive FDM*/
				R3COG27--R15COG27 /* cognitive FDM*/ 
				R3PRMEM--R15PRMEM /* proxy report for cognitive FDM*/
				R3EYERT--R15EYERT /*sensory FDM*/
				R3EARRT--R15EARRT /*sensory FDM*/
				R3CONDE--R15CONDE /* Disease Frailty Index*/
                R3ADL6A--R15ADL6A /* functional limitation FI*/
                R3IADL5A--R15IADL5A /*instrumental activities FI*/
				R3CESD--R15CESD /* Mental Impairment FI*/
                R3LBRF--R15LBRF /* retirement status*/
				R3AGEY_B--R15AGEY_B /*age at beginning of interview for each wave*/
				RARACEM /* race masked*/
				RAGENDER /* gender*/
				RAHISPAN /* hispanic (ethnicity) */
				R3MSTAT--R15MSTAT /* spouse)*/
				RAEDUC /* general education level*/
				H3ATOTB--H15ATOTB /* total wealth*/
				EXDEATHMO /*month of death*/
				EXDEATHYR /* year of death*/
				R3IWEND--R15IWEND /*interview end date*/
				R3WTRESP--R15WTRESP
				RADDATE
				INW3-INW15
				R3IWSTAT--R15IWSTAT
				H3CPL--H15CPL
				R3NHMLIV--R15NHMLIV
				RAEHSAMP
				RAESTRAT
				/* Nick here - adding some alternate month-year retirement data too */
				%waves(SAYRET)
				%waves(RETMON)
				%waves(RETYR)
				%waves(RETDTWV) /* Indicates original wave in which these particular mo/years reported */
				  /* ...Tracker birth date... */
				BIRTHMO
				BIRTHYR
				  /* ...and longitudinal dataset birth date... */
				RABDATE
     ;
run;

* convert interview date;
data outlib.rand_with_dates;
	set worklib.rand_sort_columns;
	array r_iwend[3:15] R3IWEND -- R15IWEND;
	array r_iwend_date[3:15] RIWEND_date_3 - RIWEND_date_15;

	do i = 3 to 15;
		r_iwend_date[i] = r_iwend[i];
	end;
	
	format RIWEND_date_3 - RIWEND_date_15 date9.;
	drop i R3IWEND -- R15IWEND;
run;	

data outlib.rand_with_dates;
	set outlib.rand_with_dates;
	format RADDATE date9.;
	format RABDATE date9.;
run;


proc export data = outlib.rand_with_dates
	outfile = "&outlib\rand_with_dates.csv"
	dbms = csv
	replace;
run;
