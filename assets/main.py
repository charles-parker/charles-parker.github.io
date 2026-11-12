#******************************************************************************
# Author:           Charles Parker
# Assignment:       Assignment 5- Adding a menu to the coffee program
# Date:             14 Mar 2023
# Description: Will ask for the type of coffee and return the number
# of tbsp of coffee. 
# Input:            coffee_name = string, cups_coffee = integers, 
# coffee_type = string, menu_option = integer
# Output:           tbls_coffee = integer, total_num_cups = integer
# Sources:          Assignment 5 specifications
#                
#******************************************************************************
# Constant
LIGHT_ROAST = 1
MED_ROAST = 2
DARK_ROAST = 3
MAKE_COFFEE = 1
PRINT_LIST = 2
QUIT = 3
CUP_TO_OZ = 8
ROAST_TYPE = ["light", "medium", "dark"]
import valid as v
import list as l

def main():
# Variables
  coffee_names = []
  cups_coffees = []
  coffee_types = []
  total_tbsp = 0
  tbsp_type = 0
  count = 0
  
  print_welcome()
  print_menu()
  option = get_menu_option()

  while option != QUIT:
    if option == MAKE_COFFEE:
      get_coffee_name(coffee_names)
      get_coffee_type(coffee_types)
      get_cups_coffee(cups_coffees)
      tbsp_type = calc_tbsp_type(coffee_types[count])
      total_tbsp = calc_total_tbsp(cups_coffees[count], tbsp_type)
      print_req_tbsp(coffee_names[count], cups_coffees[count], total_tbsp)
      count += 1
      print_menu()
      option = get_menu_option()
    if option == PRINT_LIST:
      print_list(coffee_names, coffee_types, cups_coffees)
      print_menu()
      option = get_menu_option()
  if option == QUIT and count == 0:
      print("\nYou entered nothing.\nHave a great day!")
  elif option == QUIT:
    light_sum = l.add_value(cups_coffees, coffee_types, ROAST_TYPE[0])
    med_sum = l.add_value(cups_coffees, coffee_types, ROAST_TYPE[1])
    dark_sum = l.add_value(cups_coffees, coffee_types, ROAST_TYPE[2])
    total_sum = light_sum + med_sum + dark_sum
    light_percent = calc_percent(light_sum, total_sum)
    med_percent = calc_percent(med_sum, total_sum)
    dark_percent = calc_percent(dark_sum, total_sum)
    max_value = l.max(cups_coffees)
    max_loc = l.find_value(cups_coffees, max_value)
    print_coffee_stats(total_sum, light_percent, med_percent, 
                       dark_percent, coffee_names[max_loc])

def print_welcome():
  """
  Prints welcome statement 
  :param:
  :return:
  """
  print("This program will figure out how many tbsp of coffee", end="")
  print(" grounds you need!")
  print("-" * 30)
  print(f"Light roast: {LIGHT_ROAST: > 2} tbsp per cup.")
  print("Medium roast:", MED_ROAST, "tbsp per cup.")
  print(f"Dark roast: {DARK_ROAST: > 3} tbsp per cup")
  print("-" * 30)


def print_menu():
  """
  Prints out the menu for the program to either make a cup of coffee, print
  a list or quit the program
  :param:
  :return:
  """
  print("-" * 30)
  print(f'{"Menu Option":^30}')
  print("\n1. Make a pot of coffee")
  print("2. Print List")
  print("3. Quit the program")
  print("-" * 30)


def get_menu_option():
  """
  This gets an input from the user to either 1. run the program or 2. print 
  list or 3 to quit
  :param:
  :return: an int assigned to option that will be either 1, 2 or 3
  """
  option = 0
  option = v.get_integer("Enter either menu choice 1, 2, or 3: ")
  while option < MAKE_COFFEE or option > QUIT:
    print("Wrong menu option. Please enter 1, 2, or 3.")
    option = v.get_integer("Enter either menu choice 1, 2, or 3: ")
  return option


def get_coffee_name(coffee_names):
  """
  Get input from the user for the name of the coffee being made.
  :param: coffee_names is a list containing coffee names stored as a string
  :return: the coffee name as a string that is stored in coffee_name list
  """
  coffee_name = ""
  coffee_name = v.get_string("\nType the brand name of the"
                            " coffee you are making: ")
  coffee_name = coffee_name.strip()
  coffee_name = coffee_name.lower()
  coffee_names.append(coffee_name)
  


def get_coffee_type(coffee_types):
  """
  Gets the coffee type assigned to coffee_types list
  :param: coffee_types is a list that contains light, medium, or dark
  :return: a string containing either light, medim, or dark that is 
  returned to the list coffee_types
  """
  type = ""
  temp = False
  index = 0
  
  while temp != True:
    index = 0
    type = v.get_string("\nEnter the type of coffee (light, medium,"
                        " or dark): ")
    type = type.strip()
    type = type.lower()
    while index < len(ROAST_TYPE):
      if type == ROAST_TYPE[index]:
        temp = True
        coffee_types.append(type)
      index += 1
    if temp == False:
      print("Wrong input. Enter either light, medium, or dark")
    


def get_cups_coffee(cups_coffees):
  """
  Gets the number of cups of coffee the user is making
  :param: cups_coffees is a list containg cups of coffee as integers
  :return: an integer that represents the cups of coffee the user entered
  and is returned to the list cups_coffees
  """
  cups = 0
  cups = v.get_integer("How many cups of coffee are you making (ex. 5): ")
  while cups <= 0 or cups > 100:
    print("You entered an invalid number cups of coffee. Please entered a" 
          " value between 1 and 100.")
    cups = v.get_integer("How many cups of coffee are you making (ex. 5): ")
  cups_coffees.append(cups)


def calc_tbsp_type(coffee_type):
  """
  Takes the coffee type and figures out how many tbsp of grounds per cup
  :param: coffee types is a list of string that will either contain light,
  medium, or dark
  :return: an integer assigned to tbsp_type based on the if/elif statement
  """
  tbsp_type = 0
  
  if coffee_type == ROAST_TYPE[0]:
    tbsp_type = LIGHT_ROAST
  elif coffee_type == ROAST_TYPE[1]:
    tbsp_type = MED_ROAST
  elif coffee_type == ROAST_TYPE[2]:
    tbsp_type = DARK_ROAST
  return tbsp_type
  
  

def calc_total_tbsp(cups_coffee, tbsp_type):
  """
  Calculates the total tbsp of coffee grounds needed to make x cups of coffee.
  :param: cups_coffees is a list containing the num of cups of coffee as 
  integer
  :param: tbsp_type is an integer assigned to one of three constants from the 
  calc_tbsp_type function
  :param: count is an integer that contains the number that the iteration 
  of the while loop is on
  :param: total_tbsps is a list containing the total number of tbsps as an 
  integer
  :return: an integer assigned to total_tbsp
  """
  num = 0
  num = cups_coffee * tbsp_type
  return num



def print_req_tbsp(coffee_name, cups_coffee, total_tbsp):
  """
  Prints a statement indicating the num of tbsp of coffee, num of cups of 
  coffee, and the coffee name.
  :param: coffee_name is a string that is a specific coffee name 
  :param: cups_coffee is the num cups of coffee as an int 
  :param: total_tbsps is an int that contains the total num of coffee grounds
  :return:
  """
  print("\nYou need", total_tbsp, "tbsp of coffee in", end = "")
  print(" order to make ", cups_coffee, "cups of ", end = "")
  print(coffee_name.title())


def  print_list(coffee_names, coffee_types, cups_coffees):
  """
  The function prints out a list that contains the coffee names, types of
  roast, number of cups of coffee and the total tbsp of coffee grounds
  :param: coffee_names is a list containing coffee names stored as a string
  :param: coffee types is a list of string that will either contain light,
  medium, or dark
  :param: cups_coffees is a list containing the num of cups of coffee as 
  integer
  :return:
  """
  i = 0
  print(f'\n{"Coffee Name":<15} {"Roast Type":<12}', end = "")
  print(f'{"Total Cups":<11} {"Total Tbsp":<10}')
  print("-" * 50)
  while i < len(coffee_types):
    tbsp_type = calc_tbsp_type(coffee_types[i])
    print(f"{coffee_names[i].title():<15} {coffee_types[i]:<15}", end = "")
    print(f"{cups_coffees[i]:<10}", end = "") 
    num = calc_total_tbsp(cups_coffees[i], tbsp_type)
    print(f"{num:<20}")
    i += 1


def print_coffee_stats(total_sum, light_percent, med_percent, 
                       dark_percent, coffee_name):
  """
  This function prints out the coffee stats when the user quits the program
  :param: total sum is an integer that contains the total number of 
  coffee the user made
  :param: coffee_name is a string that will be the coffee name associated 
  the max cups of coffee in a single sitting
  :param: light_percent contains the percent of light roast coffee made
  as a float
  :param med_percent contains the percent of med roast coffee made as a float
  :param: dark_percent contains the percent of dark roast coffee made as a 
  float
  :return:
  """                    
  print("\nThe total number cups of coffee you made is", total_sum)
  print("The most popular coffee brand you made in a single time is", 
       coffee_name.title())
  print(f"\nPercent of light roast made: {light_percent:.2f}%")
  print(f"Percent of medium roast made: {med_percent:.2f}%")
  print(f"Percent of dark roast coffee made: {dark_percent:.2f}%")



def calc_percent(sum, total_sum):
  """
  finds the percent of a sum out of the total sum
  :param: sum contains a certain amount as an integer
  :param: total_sum contains the total number cups of coffee as an int
  :return: the percent cups of a certain roast as a float
  """
  percent = 0.0
  percent = (sum / total_sum) * 100
  return percent
  

    
def print_final_message():
  """
  Prints a goodbye message
  :param:
  :return:
  """
  print("\nEnjoy your cup of coffee!")


main()