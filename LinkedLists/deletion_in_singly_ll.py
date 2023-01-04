from linked_list_impl import LinkedList, Node

lst = LinkedList()
for i in range(1, 4):
    lst.insert_at_head(i)

lst.print_list()
print(" List created ")


def delete_at_head(lst: LinkedList):
    first_elem: Node = lst.get_head()

    if first_elem:
        lst.head_node = first_elem.next_element
    first_elem.next_element = None
    return


def delete_a_value(lst: LinkedList, value):
    curr_node = lst.get_head()
    prev_node = None

    if value is None:
        print("Can not search for None in the List")
        return

    if curr_node is None:
        print("Deletion not possible as linked list is empty")
        return False

    # This means if the element to be deleted is at the head of the linked list
    if curr_node.data == value:
        lst.head = curr_node.next_element
        curr_node.next_element = None
        return True

    while curr_node:
        if curr_node.data == value:
            # delete the current node
            prev_node.next_element = curr_node.next_element
            curr_node.next_element = None
            return True

        prev_node = curr_node
        curr_node = curr_node.next_element

    print(f"Element {value} does not exists in the list")
    return False


def delete_at_tail(lst):
    if not lst:
        return False

    curr_node = lst.head_node
    prev_node = None

    while curr_node:
        if curr_node.next_element is None:
            prev_node.next_element = None
            return True
        prev_node = curr_node
        curr_node = curr_node.next_element


# delete_at_head(lst)
delete_a_value(lst, 1)
lst.print_list()

delete_at_tail(lst)
lst.print_list()
