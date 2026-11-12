// Charles Parker
// May 26, 2023
// CS162
// Programming Assingment 4


/* Data types for course library
   int course_size
   int num_of_courses
   course *course_list
*/

#include "course_library.h"

// This is the constructor for course library.
course_library::course_library()
{
	course_size = 0;
	course_list = nullptr;
	num_of_courses = 0; // the number of courses that the user wants to add
			    // asks the user how many courses they are
			    // going to add. This will be used to create
			    // the dynamically allocated array for the course list pointer
	do
	{
		cout << "\nEnter how many courses you want to add: ";
		cin >> num_of_courses;
		cin.ignore(100, '\n');
		if (num_of_courses < 1)
		{
			cout << "\nYou entered an invalid number of courses." << endl;
		}
	} while (num_of_courses < 1);
	course_list = new course[num_of_courses];
}

// This is the course deconstructor. It will deallocate the memory 
// from the course_library pointer
course_library::~course_library()
{
	if (course_list != nullptr)
		delete [] course_list;
}
// This function will allow the user to add the course info untill they chose
// to stop entering a course or they reached the max number of courses that
// they chose to entered. The function will not return anything or have any 
// arguments. 
void course_library::read_all()
{
	char option;

	if (course_size < num_of_courses)
	{
		do
		{
			if (course_size == 0)
				cout << "\nEnter Y to enter a course or N to go back to the main menu: ";
			else
				cout << "\nEnter Y to enter another course or N to go back to the main menu: ";
			cin >> option;
			cin.ignore(100, '\n');
			if (toupper(option) != 'Y' &&  toupper(option) != 'N')
			{
				cout << "\nYou entered a wrong menu option" << endl;
			}
			if (toupper(option) == 'Y')
			{
				course_list[course_size].read_course();
				++course_size;
			}
		} while (course_size < num_of_courses && toupper(option) != 'N');
		if (course_size == num_of_courses)
			cout << "\nYou reached the total numeber of courses that you entered." << endl;
		if (toupper(option) == 'N')
		{
			cout << "\nYou chose to not add another course" << endl;
		}
	}
	else if (course_size >= num_of_courses)
		cout << "\nYou already entered the max number of courses that you specified." << endl;

	return;
}


// The display all function will cycyle through the array and display the course information
// until it reached the number of courses that the user has entered. The function will not return
// anything and does not have any arguments.
void course_library::display_all()
{
	if (course_size == 0)
	{
		cout << "\nThere are no courses entered." << endl;
	}
	else if (course_size > 0)
	{
		for (int i {0}; i < course_size; ++i)
		{
			course_list[i].display_course();
		}
	}
	return;
}

void course_library::find_all()
{
	int i {0};
	int num {0};
	char search[SIZE];

	cout << "Enter the course number that you are searching for: ";
	cin.get(search, SIZE, '\n');
	cin.ignore(100, '\n');

	for (i; i < course_size; ++i)
	{
		if (course_list[i].find_course(search))
		{
			num = 1;
		}
	}
	if (num == 0)
	{
		cout << "\nThe course number is not a match" << endl;
	}
	return;
}
