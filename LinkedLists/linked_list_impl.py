# Implementation of Linked Lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if not self.head_node:
            return True
        else:
            return False

    def insert_at_head(self, data):
        temp = Node(data)
        temp.next_element = self.head_node
        self.head_node = temp
        return self.head_node

    def print_list(self):
        if self.head_node is None:
            print("Empty Linked List")
            return
        curr_node = self.head_node
        while curr_node.next_element:
            print(curr_node.data, end=" -> ")
            curr_node = curr_node.next_element
        print(curr_node.data, "-> None")


# lst = LinkedList()
# print(lst.is_empty())
