"""
We will cover 3 types of insertions:
1. Head
2. Tail
3. kth index
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self) -> Node:
        return self.head_node

    def is_empty(self) -> bool:
        if not self.head_node:
            return True
        else:
            return False

    def insert_at_head(self, data):
        # create a new temp node with data
        temp_node = Node(data)
        # New node's next element will point to the current head(or first) node
        # result: temp.next = current first element
        temp_node.next_element = self.head_node
        # Now change the head node to point to the temp node
        self.head_node = temp_node
        # result: Head -> temp -> previous_head_node
        return self.head_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        # iterate till the last node and replace its next element with the new node
        # The next element for new_node will be None
        if self.is_empty():
            self.head_node = new_node
            return True
        ll_node = self.head_node
        while ll_node.next_element:
            ll_node = ll_node.next_element
        ll_node.next_element = new_node
        new_node.next_element = None
        return True

    def insert_at_k_index(self, idx, data):
        new_node = Node(data)
        curr_idx = 0
        if self.head_node is None and idx != 0:
            print("empty linked list")
            return False
        if idx == 0:
            self.head_node = Node(data)
            return True

        curr_node = self.head_node
        prev_node = None
        while curr_node:
            if curr_idx == idx:
                prev_node.next_element = new_node
                new_node.next_element = curr_node
                return True
            curr_idx += 1
            prev_node = curr_node
            curr_node = curr_node.next_element
        # for out of range insert
        if idx > curr_idx:
            print("linked list is only of size -> ", curr_idx)
            return False

    def print_list(self):
        if self.is_empty():
            return False
        temp = self.head_node
        while temp.next_element:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True


# list = LinkedList()
# list.print_list()
#
# print("Inserting values in list")
# for i in range(1, 5):
#     list.insert_at_head(i)
# list.print_list()
#
# n = Node(100)
# list.insert_at_tail(100)
# list.print_list()
#
# l = LinkedList()
# l.insert_at_k_index(0, 100)
# l.print_list()
