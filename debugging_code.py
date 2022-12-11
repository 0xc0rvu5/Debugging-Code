#problem 1
# Instructions

#     Read this the code in main.py
#     Spot the problems 🐞.
#     Modify the code to fix the program.

# Fix the code so that it works and passes the tests when you submit.

#main.py faulty code
# number = int(input("Which number do you want to check?"))

# if number % 2 = 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")


#solution
number = int(input("Which number do you want to check?\n ~ "))

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")


#problem 2
# Instructions

#     Read this the code in main.py
#     Spot the problems 🐞.
#     Modify the code to fix the program.
#     No shortcuts - don't copy-paste to replace the code entirely with a working solution.

# Fix the code so that it works and when you hit submit it should pass all the tests.

#main.py faulty code
# year = input("Which year do you want to check?")

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")
  

#solution
year = int(input("Which year do you want to check? ~ "))


if year % 4 == 0 and year != 100 == 0 and year % 400 == 0:
    print('Leap year.')
if year % 4 == 0 and year % 100 == 0:
    print('Not a leap year.')
if year % 4 == 0:
    print('Leap year.')
else:
    print('Not leap year.')


#problem3
# Instructions

#     Read this the code in main.py
#     Spot the problems 🐞.
#     Modify the code to fix the program.
#     No shortcuts - don't copy-paste to replace the code entirely with a working solution.

# The code needs to print the solution to the FizzBuzz game.

#     Your program should print each number from 1 to 100 in turn.

#     When the number is divisible by 3 then instead of printing the number it should print "Fizz".

#     When the number is divisible by 5, then instead of printing the number it should print "Buzz".

#       And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

#main.py faulty code
# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])


#solution
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)