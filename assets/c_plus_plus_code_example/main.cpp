/* Charles Parker
 * May 23 2023
 * CS162
 * Program 4
 * This is the main.cpp file. It will contain the main function and
 * make the calls to the other .cpp files
 */

#include "menu.h"


int main()
{
	int option {0};
	menu menu;
	menu.welcome();
	course_library course_library;
	do
	{
		option = menu.menu_option();
		if (option == 1)
			course_library.read_all();
		else if (option == 2)
			course_library.display_all();
		else if (option == 3)
			course_library.find_all();
	} while (option != 4);
	menu.quit();
	return 0;
} // calls the deconstructor
