# problem statement

"""
Given an array of unsorted integers find two numbers in an array find two numbers which add upto k

Approach 1: Brute Force
For each element check if other elements add upto k. This will iterate in both inner and outer loop
TC = O(n^2)
SC = O(1) if not returning all possible values.


Approach 2: Using Hashing
Add all elements inside the hashmap.
iterate over the list
    Calculate sum - elem and lookup in hashmap to see if it exists
    In case that element is found return current num and hashmap key

TC = O(n)
SC = O(1) as we are only returning the elements and not storing them anywhere


EDUCATIVE SOLUTIONS

1. Sort the list and search
    In this solution the sort has been done only to help with binary search
    TC = O(log n) + O(nlog n) => O(nlog n)
    SC = Constant
2. Moving indices
    Use two pointers from front and back and keep checking with sum
        if sum < k
            increase the left pointer
        elif sum > k
            decrease the right pointer
        else
            return i,j
    TC = O(nlog n) as we are sorting the list before iterating over it which is the most time-consuming amongst other
        things done in the solution

"""

l1 = list(range(10, 100, 2))


def approach_1(lst, k):
    res = []
    for i in lst:
        for j in lst:
            if i + j == k:
                res.append((i, j))
                return i, j
    return res


# print(approach_1(l1, 52))


def approach_2(lst, sum):
    visited = {}
    possible_res = []
    for i in range(len(lst)):
        # elem -> index
        visited[lst[i]] = i

    for i in lst:
        j = sum - i
        if j in visited:
            possible_res.append((i, j))
            return i, j

    return possible_res


# print(approach_2(l1, 52))


def edu_approach_1(lst, k):
    for i in lst:
        j = k - i
        ind = binary_search(lst, i)
        if ind != -1 and lst[ind] != i:
            return i, lst[ind]


def binary_search(a, item):
    first = 0
    last = len(a) - 1
    found = False
    index = -1
    while first <= last and not found:
        mid = (first + last) // 2
        if a[mid] == item:
            index = mid
            found = True
        else:
            if item > mid:
                first = mid + 1
            if item < mid:
                last = mid - 1
    if found:
        return index
    else:
        return -1


def edu_approach_2(lst, k):
    ind1 = 0
    ind2 = len(lst) - 1
    res = []
    lst.sort()

    while ind1 != ind2:
        sum = lst[ind1] + lst[ind2]

        if sum < k:
            ind1 += 1
        elif sum > k:
            ind2 -= 1
        else:
            res.append(lst[ind1])
            res.append(lst[ind2])
            return res
    return []


print("eu_2", edu_approach_2(lst=l1, k=10))
