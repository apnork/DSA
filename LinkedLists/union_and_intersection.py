"""
Given two linked lists write two functions which would retunrn their union and intersection


"""
from insertion import LinkedList
from remove_duplicates import remove_duplicate


def union(lst1: LinkedList, lst2: LinkedList):
    l2_head = lst2.get_head()
    l1_node = lst1.get_head()
    # iterate to the second last element
    while l1_node.next_element:
        l1_node = l1_node.next_element
    l1_tail = l1_node

    # Extend the l1 list
    l1_tail.next_element = l2_head
    return remove_duplicate(lst1)


l1 = LinkedList()
l2 = LinkedList()
for i in range(1, 10):
    l1.insert_at_head(i)
for i in range(7, 15):
    l2.insert_at_tail(i)

l1.print_list()
l2.print_list()

# res = union(l1, l2)
# res.print_list()


def intersection(lst1, lst2):
    visited_1 = {}
    visited_2 = {}
    res = LinkedList()

    c1 = lst1.get_head()
    c2 = lst2.get_head()

    while c1:
        if c1.data not in visited_1:
            visited_1[c1.data] = 1
        c1 = c1.next_element

    while c2:
        if c2.data not in visited_2:
            visited_2[c2.data] = 1
        c2 = c2.next_element

    c1 = lst1.get_head()

    while c1:
        if c1.data in visited_2:
            res.insert_at_head(c1.data)
        c1 = c1.next_element
    print(visited_1)
    print(visited_2)
    return res


res = intersection(l1, l2)
res.print_list()
