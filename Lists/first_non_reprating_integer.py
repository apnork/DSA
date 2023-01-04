# problem statement

"""
find the first integer which is unique in the list

Approach 1:
Iterate over the list to check if there are any other same elements

"""


def approach_1(lst):
    unique_elem = 0
    for i in range(len(lst)):
        found = False
        # search the same element in the list again except it itself
        # If found increment the element and search again
        # if not found return this number
        for j in range(len(lst)):
            if i == j:
                continue
            if lst[i] == lst[j]:
                found = True
                break
        if not found:
            return lst[i]


l1 = [9, 2, 3, 9, 2, 6, 6]
print(approach_1(l1))


def approach_2(lst):
    visited = {}

    # add all elements if already present increase frequency
    for elem in lst:
        if elem in visited:
            visited[elem] = visited.get(elem) + 1
        else:
            visited[elem] = 1

    for elem in lst:
        freq = visited.get(elem)
        if freq == 1:
            return elem


print(approach_2(l1))
