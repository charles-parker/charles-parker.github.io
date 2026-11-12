// Charles Parker
// May 23, 2023
// CS162 
// Program 4
// This file will contain the course class and the associated data
// for a single course. It will also contain the function prototypes
// for a single course including: reading in a course info, displaying
// a the course info, and finding a course based on the course number

/* Data types for course
*name;
*course_number;
*pre_req;
*recommendation;
*schedule;
*/
#include "course.h"

//This is the constructor. Sets the data to a starting value
course::course()
{
	name = nullptr;
	course_number = nullptr;
	pre_req = nullptr;
	recommendation = nullptr;
	schedule = nullptr;
	temp = new char[SIZE];
}

//This is the deconstructor. This sets the value of the 
//data members back to zero
course::~course()
{
	if (nullptr != name)
		delete name;
		name = nullptr;
	if (nullptr != course_number)
		delete course_number;
		course_number = nullptr;
	if (nullptr != pre_req)
		delete pre_req;
		pre_req = nullptr;
	if (nullptr != recommendation)
		delete recommendation;
		recommendation = nullptr;
	if (nullptr != schedule)
		delete schedule;
		schedule = nullptr;
	if (nullptr != temp)
		delete temp;
		temp = nullptr;
}
// This fnction reads in the data into the temp pointer and then calls the
// make lower function and the cin.peek() sees if the user hit the enter key or not
void course::get_temp()
{
	if (cin.peek() != '\n')
	{
		cin.get(temp, SIZE, '\n');
		cin.ignore(100, '\n');
		make_lower();
	}
	return;
}
	
	
// this function will get the course info from the user. It will use
void course::read_course()
{
	// Gets the course name
	do
	{
		cout << "\nEnter the course name: ";
		get_temp();
		if (name != nullptr)
			delete name;
		name = new char[strlen(temp) + 1];
		strcpy(name, temp);
	} while (correct_info());
	temp[0] = '\0';
	// Gets the course number
	do
	{
		cout << "\nEnter the course number: ";
		get_temp();
		if (course_number != nullptr)
			delete course_number;
		course_number = new char[strlen(temp) + 1];
		strcpy(course_number, temp);
	} while (correct_info());
	temp[0] = '\0';
	// Gets the pre-req info
	do
	{
		cout << "\nEnter the course pre-requisites: ";
		get_temp();
		if (pre_req != nullptr)
			delete pre_req;
		pre_req = new char[strlen(temp) + 1];
		strcpy(pre_req, temp);

	} while (correct_info());
	temp[0] = '\0';
	// Gets the course recommendation
	do
	{
		cout << "\nEnter the course recommendations: ";
		get_temp();
		if (recommendation != nullptr)
			delete recommendation;
		recommendation = new char[strlen(temp) + 1];
		strcpy(recommendation, temp);
	} while (correct_info());
	temp[0] = '\0';
	// Gets the course schedule
	do
	{
		cout << "\nEnter the course schedule: ";
		get_temp();
		if (schedule != nullptr)
			delete schedule;
		schedule = new char[strlen(temp) + 1];
		strcpy(schedule, temp);
		
	} while (correct_info());
	temp[0] = '\0';

	return;
}
// asks the user if what the enter is correct
// if not will asks them to reenter the information
bool course::correct_info()
{
	char answer;
	do
	{
		cout << "\nEnter Y to re-enter the info or N to continue running the program: ";
		cin >> answer;
		if (answer != '\n')
		{
			cin.ignore(100, '\n');
			if (toupper(answer) != 'N' && toupper(answer) != 'Y')
				cout << "\nYou enter a wrong response." << endl;
		}
		else
			cin.ignore(100, '\n');
	} while (toupper(answer) != 'N' && toupper(answer) != 'Y');
	if (toupper(answer) == 'Y')
	{	
		cout << "\nYou entered Y to re-enter the information." << endl;
		temp[0] = '\0';
		return true;
	}
	else if (temp[0] == '\0')
	{
		cout << "\nYou can't leave the field blank." 
		     << "\nPlease enter the required information before moving on to the next field."
		     << endl;
		return true;
	}
		
	else 
	{
		cout << "\nYou enter N to continue with the program." << endl;
		return false;
	}
		
}
// makes an array that is passed all lowercase
void course::make_lower()
{
	int len = strlen(temp);
	
	for(int i = 0; i < len; ++i)
	{
		temp[i] = tolower(temp[i]);
	}
	cout << "\nYou entered: " << temp << endl;
	return;
}
// displays the course information
void course::display_course()
{
	cout << "\nCourse Information" << "\n********************" << endl;
	cout << "Course Name: " << name << "\nCourse Number: " << course_number
	     << "\nCourse Description: " << recommendation << "\nCourse Pre-reqs: " 
	     << pre_req << "\nCourse Schedule: " << schedule << endl << endl;
	return;
}
// displays the course information if the course number that the user search for
// is a match
bool course::find_course(char array[])
{
	if (strcmp(course_number, array) == 0)
	{
		cout << "\nThe course number " << temp << " is a match!" << endl;
		cout << "Here is the course information." << endl;
		display_course();
		return true;
	}
	else
	{
		return false;
	}
}
