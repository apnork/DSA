"""

You have to implement the MinStack class which will have a min() function. Whenever min() is called, the minimum
value of the stack is returned in O(1) time. The element is not popped from the stack. Its value is simply returned.



"""
# Create Stack => stack = myStack(5); where 5 is size of stack
# Create Queue => queue = myQueue(5); where 5 is size of queue
# Stack Functions => isEmpty(), isFull(), top()
# Queue Functions => enqueue(int),dequeue(),isEmpty(),getSize()
import sys
from stack_impl import Stack


class MinStack:
    # Constructor
    def __init__(self):
        # Write your code here
        self.main_stack = Stack()
        self.min_stack = Stack()

    def pop(self):
        # Write your code here
        self.min_stack.pop()
        return self.main_stack.pop()

    # Pushes value into new stack
    def push(self, value):
        # Write your code here
        self.main_stack.push(value)
        if self.min_stack.is_empty() or self.min_stack.peek() > value:
            self.min_stack.push(value)
        else:
            # This is done to keep track of min throughout the min stack
            self.min_stack.push(self.min_stack.peek())
        return True

    # Returns minimum value from new stack in constant time
    def min(self):
        # Write your code here
        if not self.min_stack.peek():
            return self.min_stack.peek()
        return None
