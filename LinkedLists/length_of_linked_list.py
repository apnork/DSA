# problem_statement

"""
Given a linked list find out its length

Input -> A linked list
Output -> Number of nodes in that list

Iterate over the length of list and increment a counter
"""

from linked_list_impl import LinkedList

ll = LinkedList()
for i in range(1, 8):
    ll.insert_at_head(i)


def length_of_list(lst):
    ctr = 0
    curr_node = lst.get_head()
    if curr_node is None:
        return 0
    while curr_node:
        ctr += 1
        curr_node = curr_node.next_element
    return ctr


print(length_of_list(ll))
