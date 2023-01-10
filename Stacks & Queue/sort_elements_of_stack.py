"""
Sort the elements of the stack so that the top remains the same but all other elements are sorted.

"""
import timeit
from stack_impl import Stack

stacc = Stack()
stacc.push(23)
stacc.push(60)
stacc.push(12)
stacc.push(42)
stacc.push(4)
stacc.push(97)
stacc.push(2)


def sort_stack(stack):
    stack.stack_list.sort(reverse=True)
    return stack


def temp_stack_sort_stack(stack):
    """
    1. create a new temp stack
    2. pop a value from main stack
    3.
    if value >= top(temp_stack)
        push this value to temp stack
    else
        pop all values from temp_stack
        push into main_stack
        at end push value in temp_stack
    4. repeat step 2~3 till main stack is not empty
    5. transfer from temp_stack to main_stack
    """
    if stack.is_empty():
        return None
    temp_stack = Stack()
    while not stack.is_empty():
        value = stack.pop()
        if value >= temp_stack.peek() and temp_stack.peek() is not None:
            temp_stack.push(value)
        else:
            while not temp_stack.is_empty() and value < temp_stack.peek():
                stack.push(temp_stack.pop())
            temp_stack.push(value)

    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return stack


res1 = sort_stack(stacc)


res1.print_stack()

stack = Stack()
stack.push(2)
stack.push(97)
stack.push(4)
stack.push(42)
stack.push(12)
stack.push(60)
stack.push(23)
stack.print_stack()
res2 = temp_stack_sort_stack(stack)
res2.print_stack()

