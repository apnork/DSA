"""
Implement a queue using stack


Solution
Take a new temp stack along with a main stack

enqueue - directly push into main stack
dequeue -
    Transfer all elements from main stack to temp stack
    pop the first element of the temp stack as it will have the oldest element
"""


from stack_impl import Stack
# Push Function => stack.push(int)  //Inserts the element at top
# Pop Function => stack.pop()       //Removes and returns the element at top
# Top/Peek Function => stack.get_top()  //Returns top element
# Helper Functions => stack.is_empty() & stack.isFull() //returns boolean


class NewQueue:
    def __init__(self):
        self.main_stack = Stack()
        self.temp_stack = Stack()

    # Inserts Element in the Queue
    def enqueue(self, value):
        # Write your code here
        self.main_stack.push(value)
        print("enqueued ", value)
        return True

    # Removes Element From Queue
    def dequeue(self):
        # Write your code here
        if self.main_stack.is_empty() and self.temp_stack.is_empty():
            return None
        # Transfer elements from main to temp
        while self.main_stack.is_empty() is False:
            self.temp_stack.push(self.main_stack.pop())

        return self.temp_stack.pop()


q = NewQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())
q.enqueue(5)
print(q.dequeue())

