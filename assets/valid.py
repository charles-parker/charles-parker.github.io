"""
The input validation module contains functions to read in and validate
for a specific data type, integer, float, and non-empty string.
"""

def get_integer(prompt="Please enter an integer: "):
  """
  Prompts for an integer and returns a valid integer
  :param prompt: Optional string to use as prompt
  :return: a valid integer
  """
  num = 0
  valid = False
  
  while not valid:
      try:
          num = int(input(prompt))
          valid = True
      except:
          print("Invalid integer.")

  return num


def get_float(prompt="Please enter a float: "):
  """
  Prompts for a float and returns a valid float
  :param prompt: Optional string to use as prompt
  :return: a valid float
  """
  num = 0
  valid = False
  
  while not valid:
      try:
          num = float(input(prompt))
          valid = True
      except:
          print("Invalid float.")

  return num

  
def get_string(prompt="Please enter a string: "):
  """
  Proompts for a string and returns a non-empty string
  :param prompt: Optional string to use as prompt
  :return: non-empty string of characters
  """
  valid = False
  chars = ""
  while not valid:
      chars = input(prompt)
      if chars != "":
          valid = True
      else:
          print("Invalid string.")
  return chars


def get_y_or_n(prompt="Please enter 'y' or 'n': "):
  """
  Prompts for 'y' or 'n' and returns 'y' or 'n'
  'Y', 'N', and all cases of 'yes' and 'no' are accepted.
  :param prompt: Optional string to use as prompt
  :return: lowercase 'y' or 'n'
  """
  answer = ""
  answer = input(prompt)
  answer = answer.lower()

  while (answer != "n" and 
         answer != "y" and 
         answer != "no" and 
         answer != "yes"):
      print("Invalid response.")
      answer = input(prompt)
      answer = answer.lower()

  return answer[0]