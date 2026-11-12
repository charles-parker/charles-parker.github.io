// Charles Parker
// May 30, 2023
// Program 4
// CS162
// This is the menu.cpp file. It will contain the different
// functions for menu and will only focus on getting the 
// right menu options from the user. Does not work on the 
// course or course list.
#include "menu.h"

// menu constructor
menu::menu()
{
	int option {0};
}
// This function will display a final message when the user
// quits the program. It will not return anything and will 
// not have any arguments.
void menu::quit()
{
	cout << "\nThank you for using the Course Planner Program!"
	     << endl;
	return;
}


// This function will display the welcome message to the user. 
// It is a void function and will not return anything.
void menu::welcome()
{
	cout << "\nWelcome to the Course Planner Program."
	     << "\nThis program will keep track of the courses"
	     << " you enter!" << endl;
	return;
}


// This funcion will get the menu option from the user and will
// return a value between 1-4. The function does not use any 
// arguments
int menu::menu_option()
{
	int option {0};

	cout << "\n1. Enter a course."
		<< "\n2. Display all courses."
		<< "\n3. Find a course."
		<< "\n4. Quit Program." << endl;
	do
	{
		cout << "Select a menu option: ";
		cin >> option;
		cin.ignore(100, '\n');
		if (option < 1 || option > 4)
		{
			cout << "You entered an invalid menu option." << endl;
		}
	} while (option < 1 || option > 4);
	return option;
}


