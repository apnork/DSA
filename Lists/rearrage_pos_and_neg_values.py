# problem statement

"""
approach 1:
collect all negative numbers and positive numbers in different lists
add them and return
TC = O(n)

approach 2:

"""


def approach_1(lst: list) -> list:
    pos = []
    neg = []

    if not lst:
        return []

    # collect in diff. lists
    for elem in lst:
        if elem < 0:
            neg.append(elem)
        else:
            pos.append(elem)

    return neg + pos


l1 = [10,-1,20,4,5,-9,-6]
print(approach_1(l1))
