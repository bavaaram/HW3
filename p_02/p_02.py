#! /usr/bin/python3
import math


# EAFP Style
def div_eafp(n_1, n_2):
    """
    This function divide two numbers./
    Implemented with EAFP style
    """
    try:
        print(float(n_1) / float(n_2))
    except ZeroDivisionError:
        print(f"Division by Zero: {math.inf}")
    except ValueError:
        print("Invalid Inputs. Please Try again.")


num1, num2 = input().split()
div_eafp(num1, num2)
