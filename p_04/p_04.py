#! /usr/bin/python3

from datetime import datetime
import jdatetime


# Taking Inputs from User
year, month, day = input("Please Enter your Birth date\
in format yyyy/mm/dd: ").split("/")
year, month, day = int(year), int(month), int(day)
print("\n************************************************\n")


# Age in Seconds
org = datetime(year, month, day)
now = datetime.now()
delta1 = (now - org).total_seconds()
print(f"You are {delta1} seconds old")
print("\n************************************************\n")

