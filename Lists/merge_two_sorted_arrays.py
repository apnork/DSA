# problem statement

"""
Implement a function that merges two sorted lists of m and n elements respectively,
 into another sorted list. Name it merge_lists(lst1, lst2).

Approach 1:
list1.append(iterate over 2nd list and keep adding)
+ sort the list

size of l1 = n
size of l2 = m

TC = m + (m+n)log(m+n) => (m+n)log(m+n)


Approach 2:
Using both the list to check which one of the lists has the smaller element, insert that element in place of the index
and increment the index of (arr1 or arr2) and res_arr
if either of the arrays still has elements remaining just copy them into the list

TC = O(m+n)


Approach 3:
Inplace Merging.
"""
l1 = list(range(10))
l2 = list(range(5, 16))


def approach_1(l1: list, l2: list) -> list:
    # iterate over l2 and keep appending to l1
    for elem in l2:
        l1.append(elem)
    l1.sort()
    return l1


def approach_2(l1, l2):
    index_arr1 = 0
    index_arr2 = 0
    index_result_arr = 0
    result = []

    # expand the result list to the combined length of both the lists
    for i in range(len(l1) + len(l2)):
        result.append(i)

    # Compare elements from both the arrays and add the smaller one in the result array

    while index_arr1 < len(l1) and index_arr2 < len(l2):
        if l1[index_arr1] < l2[index_arr2]:
            result[index_result_arr] = l1[index_arr1]
            index_arr1 += 1
            index_result_arr += 1
        else:
            result[index_result_arr] = l2[index_arr2]
            index_arr2 += 1
            index_result_arr += 1

    # Copy remaining elements of l1 into result
    while index_arr1 < len(l1):
        result[index_result_arr] = l1[index_arr1]
        index_arr1 += 1
        index_result_arr += 1

    while index_arr2 < len(l2):
        result[index_result_arr] = l2[index_arr2]
        index_arr2 += 1
        index_result_arr += 1

    return result


def approach_3(l1, l2):
    i1 = 0
    i2 = 0

    while i1 < len(l1) and i2 < len(l2):
        # insert only if l1(elem) > l2(elem)
        if l1[i1] > l2[i2]:
            l1.insert(i1, l2[i2])
            i1 += 1
            i2 += 1
        else:
            i1 += 1

    if i2 < len(l2):
        # copy all elements of l2 in l1
        l1.extend(l2[i2:])

    return l1


# print(approach_1(l1, l2))
# print(approach_2(l1, l2))
print(approach_3(l1, l2))
