# def even_or_odd(number):
#     if (number % 2) == 0:
#         return "Even"
#     else:
#         return "Odd"


# print(even_or_odd(1))  # "Odd"

# print(even_or_odd(2))  # "Even"

# print(even_or_odd(-1))  # "Odd"

# print(even_or_odd(-2))  # "Even"

# print(even_or_odd(0))  # "Even"
# def string_to_array(s):
#     array = s.split(" ")
#     return array

# String = "Emmanuel is the shit"
# newList = string_to_array(String)
# print(newList)
# array = list(range(5, 0, -1))
# print(array)
"""
Build a function that returns an array of integers from n to 1 where n>0.

Example : n=5 --> [5,4,3,2,1]
"""
# def reverse_seq(n):
#     if(n>0):
#         return list(range(n, 0, -1))

"""
Convert boolean values to strings 'Yes' or 'No'.
"""
# def bool_to_word(bool):
#     return "Yes" if bool else "No"
"""
Summation
Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0. Your function only needs to return the result, what is shown between parentheses in the example below is how you reach that result and it's not part of it, see the sample tests.

For example (Input -> Output):

2 -> 3 (1 + 2)
8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)
"""


# def summation(num):
#     #     result = 0
#     #     for n in range(0, num):
#     #         result += n
#     return num * (num + 1) // 2


# print(summation(3))

"""
The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.

Examples(Operator, value1, value2) --> output
('+', 4, 7) --> 11
('-', 15, 18) --> -3
('*', 5, 5) --> 25
('/', 49, 7) --> 7
"""
# def basic_op(operator, value1, value2):
#     if (operator == "+"): #Addtion
#         return value1 + value2
#     elif(operator == "-"): #Subtraction
#         return value1 - value2
#     elif(operator == '*'): #Multiplication
#         return value1 * value2
#     elif (operator == "/"): #Division
#         return value1 / value2
#     else:
#         return "Please enter a correct input"

# def basic_op(operator, value1, value2):
#     return eval("{}{}{}".format(value1, operator, value2))
# def basic_op(o, a, b):
#     return {'+':a+b,'-':a-b,'*':a*b,'/':a/b}.get(o)
# def basic_op(operator, value1, value2):
#     match operator:
#         case '+':
#             return value1 + value2
#         case '-':
#             return value1 - value2
#         case '*':
#             return value1 * value2
#         case '/':
#             return value1 / value2
# def basic_op(operator, value1, value2):
#     ops = {'+': lambda a, b: a + b,
#            '-': lambda a, b: a - b,
#            '*': lambda a, b: a * b,
#            '/': lambda a, b: a / b}
#     return ops[operator](value1, value2)
"""
Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. 
It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and 
Thymine ('T').

Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from 
DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic 
acid Uracil ('U').

Create a function which translates a given DNA string into RNA.

For example:

"GCAT"  =>  "GCAU"
The input string can be of arbitrary length - in particular, it may be empty. All input is guaranteed
 to be valid, i.e. each input string will only ever consist of 'G', 'C', 'A' and/or 'T'. 
"""

# def dna_to_rna(dna):
#     rna = dna.replace('T', 'U')
#     return rna

"""
Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.
"""
# def find_average(numbers):
#     # your code here
#     if not(numbers):
#         return 0
#     else:
#         return sum(numbers) / len(numbers)
# def find_average(array):
#     return sum(array) / len(array) if array else 0
# def find_average(array):
#     try:
#         return sum(array) / len(array)
#     except ZeroDivisionError:
#         return 0
"""
You will be given an array a and a value x. All you need to do is check whether 
the provided array contains the value.
Array can contain numbers or strings. X can be either.
Return true if the array contains the value, false if not. 
"""
# def check(seq, elem):
#     return (elem in seq)
# def check(list, x):
#     while True:
#         if x in list:
#             return True
#         else:
#             return False
#     pass
"""
Given an array of integers as strings and numbers, return the sum of the array values as 
if all were numbers.

Return your answer as a number. 
"""
# def sum_mix(arr):
#     return sum(int(i) for i in arr)
#  def sum_mix(arr):
#     return sum(map(int, arr))
