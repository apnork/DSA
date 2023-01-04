"""
Remove duplicates from a linked list
input - a singly linked list
output - a singly linked list with no duplicates


iterate through the linked list and add elements to a set/dict
    if the same element is found in the dict:
        delete that element (Need to track the previous element)
        prev.next = current.next
        current.next = None


1 -> 2 -> 3 -> 3 -> 4 -> 5 -> None

d = {1, 2, 3}


"""
from insertion import LinkedList


def remove_duplicate(lst: LinkedList):
    curr_node = lst.get_head()
    if curr_node is None:
        return None
    prev_node = None
    visited = {}
    while curr_node:
        if curr_node.data in visited:
            prev_node.next_element = curr_node.next_element
            curr_node.next_element = None
            curr_node = prev_node.next_element
        else:
            visited[curr_node.data] = 1
            prev_node = curr_node
            curr_node = curr_node.next_element

    return lst


ll = LinkedList()
ll.insert_at_head(1)
ll.insert_at_head(2)
ll.insert_at_head(2)
ll.insert_at_head(3)
ll.insert_at_head(3)
ll.insert_at_head(4)
# ll.print_list()
res = remove_duplicate(ll)
# res.print_list()
