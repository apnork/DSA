"""
In the find_nth function, a certain N is specified as an argument.
You simply need to return the node which is N spaces away from the None end of the linked list.

"""
from linked_list_impl import LinkedList


def nth_element_from_end(lst: LinkedList, n: int):
    if lst.is_empty():
        return None

    length = lst.length()
    if n > length:
        print("n cannot be greater than length of list")
        return None
    # position in linked list starting from head
    position = length - n + 1
    ctr = 0
    curr_node = lst.get_head()
    while curr_node:
        ctr += 1
        if ctr == position:
            return curr_node.data
        curr_node = curr_node.next_element
    return None


ll = LinkedList()
for i in range(1,5):
    ll.insert_at_head(i)
ll.print_list()
print(ll.length())
print(nth_element_from_end(ll, 1))
