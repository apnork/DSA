# problem statement
"""Max Min List Implement a function called max_min(lst) which will re-arrange the elements of a sorted list such
that the 0th index will have the largest number, the 1st index will have the smallest, and the 2nd index will have
second-largest, and so on. In other words, all the even-numbered indices will have the largest numbers in the list in
descending order and the odd-numbered indices will have the smallest numbers in ascending order.

Input -
A sorted list of size n

Output -
Max min list

[1,2,3,4] -> [1,2] [3,4]
iterate forward in first list and backwards in second list.

[4, 1, 3, 2]

[1,2,3,4,5] -> [5,1,4,2,3]

Approach 1:
Divide the list in half
if even number of elements:
    floor(size - 1)/2
if odd no of elem:
    size/2

while index1 < l1.size && index2 < l2.size:
    res.append(l2[index2])
    res.append(l1[index1])
    index1 += 1
    index2 += 1

return res
"""


def approach_1(lst):
    res = []
    ind1 = 0
    ind2 = len(lst) - 1
    if len(lst) % 2 == 0:
        split = len(lst) // 2 - 1
    else:
        split = len(lst) // 2

    print(split)
    l1 = lst[:2]
    l2 = lst[2:]

    # while ind1 < split < ind2:
    #     # if ind1 > ind2:
    #     #     break
    #     res.append(lst[ind2])
    #     res.append(lst[ind1])
    #     ind2 -= 1
    #     ind1 += 1

    for i, j in l1 and l2:
        print(i, j)

    return res


l1 = list(range(4))
# print(approach_1(l1))


def approach_2(lst):
    i1 = 0
    i2 = len(lst) - 1
    res = []
    div = len(lst) % 2
    while i1 <= i2:
        if i1 == i2:
            if div == 0:
                break
            else:
                res.append(lst[i2])
                break
        res.append(lst[i2])
        res.append(lst[i1])
        i2 -= 1
        i1 += 1
    return res


print(approach_2(l1))
