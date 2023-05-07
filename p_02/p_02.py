#! /usr/bin/python3
import math


# EAFP Style
def div_eafp(n_1, n_2):
    """
    This function divide two numbers./
    Implemented with EAFP style
    """
    try:
        print(f"Answer is: {float(n_1) / float(n_2)}")
    except ZeroDivisionError:
        print(f"Division by Zero: {math.inf}")
    except ValueError:
        print("Invalid Inputs. Please Try again.")


# LBYL Style
def div_lbyl(n_1, n_2):
    """
    This function divide two numbers./
    Implemented with LBYL style
    """
    if float(n_2) == 0:
        print(f"Division by Zero: {math.inf}")
    elif isinstance(n_1, str) or isinstance(n_2, str):
        print("Invalid Input. Please Try again.")
    else:
        print(f"Answer is: {float(n_1) / float(n_2)}")


stat = input("Please select style eafp/lbyl   ")
num1, num2 = input().split()
if stat not in ("eafp", "lbyl"):
    print("unknown stat, please try again/")
if stat == "eafp":
    div_eafp(num1, num2)
elif stat == "lbyl":
    div_lbyl(num1, num2)
