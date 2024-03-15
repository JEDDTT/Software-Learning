"""Module providing a function adding and printing two variables."""
def add(number1, number2):
    """A function adding two variables"""
    return number1 + number2

NUM1 = 4
NUM2 = 5
TOTAL = add(NUM1, NUM2)
print(f"The sum of {NUM1} and {NUM2} is {TOTAL}" + '\n')
