# problem statment
"""
Find the middle node of the linked list
if even elems:
    l/2
else
    l/2 + 1
"""
from insertion import LinkedList


def find_middle_node(lst: LinkedList):
    curr_node = lst.get_head()

    if curr_node is None:
        print("empty linked list")
        return None
    ctr = 0

    while curr_node:
        ctr += 1
        curr_node = curr_node.next_element
    curr_node = lst.get_head()

    if ctr % 2 == 0:
        node_position = int(ctr//2)
    else:
        node_position = int(ctr//2) + 1
    ctr = 1
    while curr_node:
        if ctr == node_position:
            return curr_node.data
        ctr += 1
        curr_node = curr_node.next_element

    print("Not found")
    return None


ll = LinkedList()
for i in range(0, 5):
    ll.insert_at_head(i)
ll.print_list()
print(find_middle_node(ll))

# Educative Solution
def two_pointers(lst: LinkedList):
    curr_node = lst.get_head()
    # No Data in the list
    if curr_node is None:
        return -1
    # just one Node in the list
    if curr_node.next_element is None:
        return curr_node.data

    mid_node = curr_node
    curr_node = curr_node.next_element.next_element

    while curr_node:
        mid_node = mid_node.next_element
        curr_node = curr_node.next_element
        # This can lead to accessing the next_element of None type which is an exception
        #curr_node = curr_node.next_element.next_element
        if curr_node:
            curr_node = curr_node.next_element

    if mid_node:
        return mid_node.data
    return -1


print(two_pointers(ll))
