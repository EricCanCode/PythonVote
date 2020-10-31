"""This app allows a user to find out if they are eligible to vote,
and takes them through the registration process if they are."""

import sys

print("*********************************************************+")
print("Welcome to the Python Voter Registration Application\n")
try:
    age = int(input("Please enter your age to begin or press 0 to exit.\n"))
    if age == 0:
        sys.exit("Thank you for trying the Python Voter Registration Application")
except ValueError as age_error:

    age = int(input("An age must be entered to proceed or 0 to exit.\n"))

    if age < 18:
        print("I'm sorry, voters must be 18 years of age to vote")
        sys.exit("Under Age")
    else:
        if age > 105:
            age_check = input("Are you sure you are over the age 105? Enter <Y> or <N>\n")
            if age_check.capitalize() == "Y":
                sys.exit("I'm sorry, voters of this age can not be verified using this application")
            else:
                age = int(input("Please reenter your age\n"))

f_name = input("Please enter your first name or enter 0 to exit.\n")
if f_name == "0":
    sys.exit("Thank you for trying the Python Voter Registration Application")
while not f_name:
    f_name = input("Please enter your first name or enter 0 to exit.\n")

l_name = input("Please enter your last name or enter 0 to exit.\n")
if l_name == "0":
    sys.exit("Thank you for trying the Python Voter Registration Application")
while not l_name:
    l_name = input("Please reenter your last name or enter 0 to exit.\n")

citizenship = input("Are you a U.S. Citizen? Enter <Y>, <N>, or 0 to exit\n")
if citizenship == "0":
    sys.exit("Thank you for trying the Python Voter Registration Application")
while citizenship.capitalize() != "Y" and citizenship.capitalize() != "N":
    citizenship = input("Are you a U.S. Citizen? Enter <Y>, <N>, or 0 to exit\n")

state = input("Please enter your state of residence \'2 Letters i.e. MD, or 0 to exit\n")
if state == "0":
    sys.exit("Thank you for trying the Python Voter Registration Application")
while len(state) != 2:
    print("State needs to be in 2 letter format.\n")
    state = input("Please reenter your state of residence \'2 Letters i.e. MD.\n")

try:
    zipcode = int(input("Please enter your 5 digit zipcode or 0 to exit.\n"))
    if zipcode == 0:
        sys.exit("Thank you for trying the Python Voter Registration Application")
except ValueError as zip_error:
    zipcode = int(input("Zipcode must be entered to proceed or 0 to exit.\n"))
while zipcode:
    if 100000 > zipcode > 9999:
        break
    else:
        zipcode = int(input("Please enter your 5 digit zipcode or 0 to exit.\n"))

confirm = input("Would you like to proceed? Enter <Y> or <N>\n")
if confirm.capitalize() == "Y":
    print("Here is a summary of your entered information.\n")
    print("Name: " + f_name.capitalize() + ", " + l_name.capitalize() + "\n")
    print("Age: " + str(age) + "\n")
    print("Zipcode: " + str(zipcode) + "\n")
    print("State: " + state + "\n")
    if citizenship.capitalize() == "Y":
        print("U.S. Citizen: Yes\n")
    else:
        print("U.S. Citizen: No\n")
    if str(citizenship) == "n" and "N":
        print("I'm sorry " + f_name.capitalize() +
              ". You do not qualify to register to vote with the "
              "Python Voter Registration App.\n")
        sys.exit("Not Qualified")
    else:
        print("Congratulations " + f_name.capitalize() +
              ". You qualify to register to vote with the "
              "Python Voter Registration App.\n")
else:
    sys.exit("Thank you for trying the Python Voter Registration Application")

register = input("Would you like to complete registration, enter <Y> or <N>\n")
if register.capitalize() == "Y":
    print("Your registration is complete, "
          "please allow 2-3 weeks for your card to arrive")
else:
    sys.exit("Thank you for trying the Python Voter Registration Application")
