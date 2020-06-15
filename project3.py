#! python
import sys

name = input("Enter your name:")
print (name)
year_of_born = int(input("What's the year you were born?"))
age = 2020 - year_of_born
print("You will be {} years old this year!".format(age))
