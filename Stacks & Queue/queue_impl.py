class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None
        self.prev_element = None


class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None
        self.length = 0

    def is_empty(self):
        if self.head_node:
            return False
        else:
            return True

    def get_head(self):
        if self.is_empty():
            return False
        return self.head_node.data

    def get_tail(self):
        if self.tail_node is None:
            return False
        return self.tail_node

    def insert_at_tail(self, data):
        temp_node = Node(data)
        if self.is_empty():
            self.head_node = temp_node
            self.tail_node = temp_node
        else:
            self.tail_node.next_element = temp_node
            temp_node.prev_element = self.tail_node
            # The next element of temp node is already None
            # temp_node.next_element = None
            self.tail_node = temp_node
        self.length += 1
        return temp_node.data

    def remove_head(self):
        if self.is_empty():
            return False
        node_to_remove = self.head_node
        if self.length == 1:
            self.head_node = None
            self.tail_node = None
        else:
            next_elem = node_to_remove.next_element
            next_elem.prev_element = None
            node_to_remove.next_element = None
            self.head_node = next_elem
        self.length -= 1
        return node_to_remove.data

    def __str__(self):
        val = ""
        if self.is_empty():
            return ""
        curr_node = self.head_node
        val += "[" + str(curr_node.data) + ", "
        curr_node = curr_node.next_element

        while curr_node.next_element:
            val = val + str(curr_node.data) + ", "
            curr_node = curr_node.next_element

        val = val + str(curr_node.data) + "]"
        return val


class Queue:
    def __init__(self):
        self.items = DoublyLinkedList()

    def is_empty(self):
        return self.items.is_empty()

    def front(self):
        if self.is_empty():
            return False
        return self.items.head_node

    def rear(self):
        if self.is_empty():
            return False
        return self.items.get_tail()

    def size(self):
        return self.items.length

    def enqueue(self, data):
        return self.items.insert_at_tail(data=data)

    def dequeue(self):
        if self.items.is_empty():
            return
        return self.items.remove_head()
