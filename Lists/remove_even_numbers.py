# problem statement
"""
for a list consisting of integers return a list with only odd numbers

Simple solution or non pythonic
-> iterate over elements and check if the number is odd or even and add it in a new list.

Pythonic Solution
Using a list comprehension iterate over the array and find out the odd numbers
"""


def remove_even_np(lst):
    res = []
    for i in lst:
        if i % 2 != 0:
            res.append(i)
    return res


def remove_even_py(lst):
    # newList = [expression(i) for i in oldList if filter(i)]
    return [num for num in lst if num % 2 != 0]
