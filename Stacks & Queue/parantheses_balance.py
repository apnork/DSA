"""
Problem Statement

Check if the parentheses are balanced or not

Ex:
"{[({})]}"


brute-force:
if len(str) is odd:
    return False

save the pair of left pths in dict

take one pointer at start and one at end
traverse and compare
    if they are not equal:
        return False

return True

TC = length of exp



"""
from stack_impl import  Stack


def brute_force_approach(exp) -> bool:
    if len(exp) % 2 != 0:
        return False
    d = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    p = 0
    q = len(exp) - 1
    while p <= q:
        # Check if last element is same as first elements value from dict
        value_from_dict = d[exp[p]]
        if exp[q] != value_from_dict:
            return False
        p += 1
        q -= 1
    return True


print(brute_force_approach("{[({})]}"))
print(brute_force_approach("(((((({{{({})}}}))))))"))


def stack_solution(exp):
    d = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    if len(exp) % 2 != 0:
        return False
    l_stack = Stack()
    # push first half of exp in stack
    for c in exp[:len(exp)//2]:
        l_stack.push(c)
    # create a list of closing characters
    comp = list(exp[len(exp)//2:])
    for e in comp:
        from_stack = l_stack.pop()
        if e != d[from_stack]:
            return False

    return True


print(stack_solution("{[({})]}"))
print(stack_solution("(((((({{{({})}}}))))))"))
