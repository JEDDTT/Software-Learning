""" def safe_divide(a, b):
    try:
        result= a / b 
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
# Test case
numerator= int(input("Please enter the numerator: "))
denominator= int(input("Please enter denominator: "))
print(safe_divide(numerator, denominator)) """

""" import math
def squareroot (number1):
    try:
        result = math.sqrt(number1)
        print(f"Result: {result}")
    except ValueError:
        print("Invalid input! Please enter a positite integer or a float value")
number = float(input("Please enter a positive or a float number:- "))
print(squareroot(number)) """

def complex_cal (num):
    try:
        result = num / (num - 5)
        print(f"Result: {result}")
    except Exception as e:
        print("An error has occured during the calculation")
#Test case
user_input = float(input("Please enter a number:- "))
complex_cal(user_input)