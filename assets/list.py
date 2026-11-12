#This module contains different functions for performing functions on
#lists


def sum(list):
  """
  This function iterates through the list and figure out the total
  of sum of a list.
  :param: a list that contains integers
  :return: the total sum as an integer
  """
  index = 0
  sum = 0
  while index < len(list):
    sum = sum + list[index]
    index += 1
  return sum


def max(list):
  """
  This functions find the max value inside a list.
  :param: a list that contains integers
  :return: an integer assigned to max that contains the max value
  """
  index = 0
  max = list[0]
  while index < len(list):
    if list[index] > max:
      max = list[index]
    index += 1
  return max


def find_value(list, value):
  """
  This functions finds an element in a list and returns the location of 
  the element
  :param: a list that contains a set of elements
  :param: a value that will be use to search through the list
  :return: the locations of the value as an integer or -1 meaning that
  the value is not in the list
  """
  loc = -1
  index = 0
  while index < len(list):
    if value == list[index]:
      loc = index
    index += 1
  return loc


def add_value(list, roast, value):
  """
  The function adds the sum of the elements inside a list if the element
  is equal to a certain value
  :param: a list that contains a set of elements
  :param: a value that will be use to search through the list
  :return: an integer assigned to sum 
  """
  index = 0
  loc = -1
  sum = 0
  while index < len(list):
    if value == roast[index]:
      loc = index
      sum = sum + list[loc]
    index += 1
  return sum