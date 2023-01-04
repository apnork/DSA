# problem statement

"""

Implement a function right_rotate(lst, k) which will rotate the given list by k.
This means that the right-most elements will appear at the left-most position in the list and so on.
 You only have to rotate the list by one element at a time.


l = [1,4,7,0,6,-1]

approach 1:
insert the popped element k times
k can be removed by taking mod of the k with len(list) if k is bigger than size of list
TC = O(n)


approach 2:
using list slicing
Total number of rotations that has to be done on the list can be reduced if we take the mod of the k with length of list
After we get the k slice the list at k to get two parts
return 2nd part + 1st part
"""


def approach_1(lst: list, k: int) -> list:
    """
    Rotates the list by k elements
    :param lst: list of integers
    :param k: number of rotations
    :return: list after rotating elements
    """
    if not lst:
        return []
    # rotations = 0
    if k > len(lst):
        rotations = k % len(lst)
    elif k == len(lst):
        return lst
    else:
        rotations = k

    for i in range(rotations):
        lst.insert(0, lst.pop())

    return lst


l1 = [10, 20, 30, 40, 50]
r = 999

print(approach_1(l1, r))
