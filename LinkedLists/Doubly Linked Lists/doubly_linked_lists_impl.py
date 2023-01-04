class Node:
    def __init__(self, data):
        self.data = data
        self.previous_element = None
        self.next_element = None


class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if not self.head_node:
            return True
        else:
            return False

    def print_list(self):
        if not self.head_node:
            return "Empty list"
        curr_node = self.head_node
        while curr_node:
            print(curr_node.data, end=" <-> ")
            curr_node = curr_node.next_element
        print("None")

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head_node is None:
            self.head_node = new_node
            self.tail_node = new_node
            return True

        new_node.next_element = self.head_node
        self.head_node.previous_element = new_node
        self.head_node = new_node
        return True

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head_node is None:
            self.head_node = new_node
            self.tail_node = new_node
            return True

        new_node.next_element = None
        new_node.previous_element = self.tail_node
        # back link or setting the next element of every previous node as the new node
        new_node.previous_element.next_element = new_node
        self.tail_node = new_node
        return True


l = DoublyLinkedList()
# for i in range(1, 5):
#     l.insert_at_head(i)
# l.print_list()
# print(l.head_node.data)
# print(l.tail_node.data)
for i in range(1, 5):
    l.insert_at_tail(i)
l.print_list()

print(l.head_node.data)
print(l.tail_node.data)

