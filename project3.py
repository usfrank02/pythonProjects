#! python
import sys

name = input("Enter your name:")
print (name)

#Request user to input the year he was born
year_of_born = int(input("What's the year you were born?"))

#Calculate the age of the user
age = 2020 - year_of_born
print("You will be {} years old this year!".format(age))
