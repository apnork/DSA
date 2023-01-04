from insertion import Node, LinkedList

lst = LinkedList()
for i in range(1, 10):
    lst.insert_at_head(i)

lst.print_list()


# Input - A linked list and an integer to be searched.


def search_element(linked_list: LinkedList, value):
    if linked_list.is_empty():
        return False
    ll_node = linked_list.get_head()
    # iterate through the list and check if any node has the value
    while ll_node:
        if ll_node.data == value:
            return True
        ll_node = ll_node.next_element

    # Last case for the end of linked list
    if ll_node is None:
        return False


def search_elem_rec(node, value):
    # base case
    if not node:
        return False

    # check if the node's data is same as value
    if node.data == value:
        return True
    # recursive call
    return search_elem_rec(node.next_element, value)


print(search_element(lst, 10))
print(search_elem_rec(lst.get_head(), 8))
