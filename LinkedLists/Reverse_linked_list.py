# Problem Statement

"""
implement a reverse() function that reverses a singly linked list

input -> linked list
output -> reversed linked list

0->1->2->3->4

4->3->2->1->0

Approach 1:
Create a new linked list and keep inserting at tail while tracking both head and tail node
TC -> O(n)
SC -> O(n)


Approach 2:
In place pointer manipulation
"""
from insertion import LinkedList


def approach_1(lst) -> LinkedList:
    new_ll = LinkedList()
    curr_node = lst.get_head()
    if curr_node is None:
        return LinkedList()
    while curr_node:
        new_ll.insert_at_head(curr_node.data)
        curr_node = curr_node.next_element
    return new_ll


def approach_2(lst):
    prev = None
    curr = lst.get_head()
    next = None

    while curr:
        next = curr.next_element
        curr.next_element = prev    # reversal
        prev = curr     # for use in next iteration
        curr = next     # increment the loop
        lst.head_node = prev
    return lst


link_list = LinkedList()
for i in range(1,6):
    link_list.insert_at_head(i)
link_list.print_list()
res_ll = approach_1(link_list)
res_ll.print_list()

res_2_ll = approach_2(link_list)
res_2_ll.print_list()
