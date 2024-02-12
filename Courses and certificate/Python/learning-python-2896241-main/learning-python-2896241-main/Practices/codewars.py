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


def summation(num):
    #     result = 0
    #     for n in range(0, num):
    #         result += n
    return num * (num + 1) // 2


print(summation(3))
