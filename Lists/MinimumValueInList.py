# problem statment
"""
Find the minimum value in a given list

approach 1:
sort the list and return the first value
TC = O(nlog n)


approach 2:
Iterate through the list and compare element to the min and save it if it is less than min
TC = O(n)
"""
import random


def approach_1(lst):
    lst.sort()
    return lst[0]


def approach_2(lst):
    min = lst[0]
    for elem in lst:
        if elem < min:
            min = elem

    return min


l1 = [1, 5, 1, -8, 0, -1, 2, 45, 6, 2]
l2 = [100, 12, 34, 40]
print(approach_1(l1))
print(approach_2(l1))
print(approach_2(l2))
