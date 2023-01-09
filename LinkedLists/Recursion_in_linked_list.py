# from linked_list_impl import LinkedList
from linked_list_impl import Node


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if self.head_node is None:
            return True
        else:
            return False

    def insert_at_head(self, data):
        temp_node = Node(data)
        if self.is_empty():
            self.head_node = temp_node
            return self.head_node
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node

    def print_list(self):
        if self.is_empty():
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True

    def recursion(self, node):
        if node.next_element is None:
            print(node.data)
            return
        self.recursion(node.next_element)
        print(node.data, node.next_element)

    def reverse(self, node):
        if node.next_element is None:
            self.head_node = node
            return None
        self.reverse(node.next_element)
        print(node.data, node.next_element.data)
        """
        This will use the recursion stack to move from end to beginning of the list.
        Using the node.next_element we will go till the last element and then the flow is returned 
        which triggers the stack pop for all the other calls.
        This means the call for the second last element will start and code after the recursive call will be executed
        
        {
            Here we create a temp node which will point to the next of second last => last element
            Next we flip the next_element of the last node to second last node => temp.next_element = node
            Then we set the current node's next_element as None
        }
        This process will repeat for all the calls that were present in the stack.
        At the last call i.e. the first element as per the last statment node.next_element = None, it's next element will
        automatically set to None
        """
        # this will only traverse till second last node
        temp = node.next_element
        temp.next_element = node # reversal now 2 points to 1
        node.next_element = None


linked_list = LinkedList()
for i in range(1, 6):
    linked_list.insert_at_head(i)

linked_list.print_list()
linked_list.reverse(linked_list.get_head())
linked_list.print_list()

# linked_list.recursion(linked_list.get_head())
