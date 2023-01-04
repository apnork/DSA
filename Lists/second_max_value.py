# problem statement

"""
Find the second maximum element in an array

Approach 1:
Sort the array and return the second last element of the list. but will have a bug
TC = O(nlog n) where n is the size of the array

Approach 2:
Iterating over the array only once and keeping track of max 1 and max 2 values
TC = O(log n)


Approach 3:
Iterating over the list twice
    1. To find the max
    2. To find the second max wrt first max
"""


def approach_1(lst):
    # drawback will fail for duplicates unless a set is used here
    lst.sort()
    return lst[-2]


def approach_2(lst):
    if not lst:
        return None

    max_1 = float('-inf')
    max_2 = float('-inf')

    for elem in lst:
        if elem > max_1:
            max_2 = max_1
            max_1 = elem
        elif elem > max_2 and elem != max_1:
            max_2 = elem

    return max_2


def approach_3(lst):
    max_1 = float('-inf')
    max_2 = float('-inf')

    for elem in lst:
        if elem > max_1:
            max_1 = elem

    for elem in lst:
        if elem > max_2 and elem != max_1:
            max_2 = elem

    return max_2


l1 = [9, 2, 6, 3]
print(l1)
# print(approach_1(l1))
# print(l1)

# print(approach_2(l1))
print(approach_3(l1))
