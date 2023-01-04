# problem statment

"""
Implement a function, find_product(lst),
which modifies a list so that each index has a product of all the numbers present in the list except the number stored
 at that index.

l1 = [2, 5, 1, 3]
sol = [15, 6, 30, 10]

- save the index which I want to skip
- if I arrive at that index continue

How do I start from the beginning always?

while index <= len(a):
    iterate on index from starting of the array till the end
    skip if i == index

"""


# l1 = [1, 2, 3]
# res = [1]


def approach_1(lst: list) -> list:
    index = 0
    res = lst
    while index < len(lst):
        for i in range(len(lst)):
            if i != index:
                res[index] *= lst[index]
        index += 1

    return res


# print(approach_1([1, 2, 3, 4]))


def approach_2(lst):
    """
    add into hashmap
    index -> elem
    """
    index = 0
    am = {}
    for i in range(len(lst)):
        am[i] = lst[i]

    prod = 0
    for key in am.keys():
        if key != index:
            prod = am[key]


def ap_3(lst):
    res = []
    for i in range(len(lst)):
        prod = 1
        for j in range(len(lst)):
            if i != j:
                prod = prod * lst[j]

"""
For each element calculate the product of all right elements of that element 
after 
"""
def edu_approach_1(lst):
    result = []
    left = 1
    for i in range(len(lst)):
        current_prod = 1
        for elem in lst[i + 1:]:
            current_prod *= elem
        # left product * right product
        result.append(current_prod * left)
        left = left * lst[i]

    return result


l1 = [1, 2, 3, 4]
r = edu_approach_1(l1)
print(r)


def edu_approach_2(lst):
    left = 1
    product = []
    # create a new list with products of all elements to the left of each element
    for ele in lst:
        product.append(left)
        left *= ele

    # Then multiply each element in that list to the product of all the elements to the right
    # of the list by traversing it in reverse
    right = 1
    for i in range(len(lst) - 1, -1, - 1):
        product[i] *= right
        right *= lst[i]

    return product
