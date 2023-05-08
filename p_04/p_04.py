#! /usr/bin/python3

from datetime import datetime
import jdatetime


# Taking Inputs from User
year, month, day = input("Please Enter your Birth date\
in format yyyy/mm/dd: ").split("/")
year, month, day = int(year), int(month), int(day)
print("\n************************************************\n")
