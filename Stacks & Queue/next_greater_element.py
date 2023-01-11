"""
Problem statment

Implement a function which takes in a list and returns a list in which each element is replaced by its next greater
element
NOTE: the function finds the first element to its right which is greater than element i
Ex: [1,3,8,4,10,5]




"""
from stack_impl import Stack


def next_greater_element(lst):
    stack = Stack()
    res = [-1] * len(lst)
    # Reverse iterate list
    for i in range(len(lst) - 1, -1, -1):
        ''' While stack has elements and current element is greater 
        than top element, pop all elements
         This means that all the elements in the stack are smaller than the lst[i]
         '''
        while not stack.is_empty() and stack.peek() <= lst[i]:
            stack.pop()
        ''' If stack has an element, top element will be 
        greater than ith element '''
        if not stack.is_empty():
            res[i] = stack.peek()
        # push in the current element in stack
        stack.push(lst[i])
    for i in range(len(lst)):
        print(str(lst[i]) + " -- " + str(res[i]))
    return res


if __name__ == "__main__":
    nge = next_greater_element([4, 6, 3, 2, 8, 1])
