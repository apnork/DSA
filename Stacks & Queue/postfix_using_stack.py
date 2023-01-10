"""
Problem Statement
The usual convention followed in mathematics is the infix expression. Operators like + and * appear between the
two numbers involved in the calculation:

6 + 3 * 8 - 4 Another convention is the postfix expression where the operators appear after the two numbers involved
in the expression. In postfix, the expression written above will be presented as:

6 3 8 * + 4 -
The two digits preceding an operator will be used with that operator

From the first block of digits 6 3 8, we pick the last two which are 3 and 8.
Reading the operators from left to right, the first one is *. The expression now becomes 3 * 8
The next number is 6 while the next operator is +, so we have 6 + 8 * 3.
The value of this expression is followed by 4, which is right before -. Hence we have 6 + 8 * 3 - 4.
Implement a function called evaluatePostFix() that will compute a postfix expression given to it as a string.

Input A string containing a postfix mathematic expression. Each digit is considered to be a separate number, i.e.,
there are no double-digit numbers.

Input = "921 * - 8 - 4 +"
Output = 3

[921]
[9] *
    res += 2 * 1
[9] -
    -> Check if size > 2 otherwise use res
    9 - res
[]
[8]
    8 - res
[]
[4]
[4] +
    4 + res

return res

for char in string:
    if '0' < char < '9':
        push into stack
    else
       if stack size >= 2:
            a = pop
            b = pop
            res += opr(a?b)
       else
            a = pop
            res = res + (opr(a?res))

return res
tc = n * k
sc = k

"""
from stack_impl import Stack
import operator


# incorrect or has bugs
def solution(exp: str):
    opr = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod
    }
    res = 0
    num_stack = Stack()

    for c in exp:
        a = 0
        b = 0
        if '0' <= c <= '9':
            num_stack.push(int(c))
        else:
            if num_stack.size() >= 2:
                a = num_stack.pop()
                b = num_stack.pop()
                if c == '/' and b == 0:
                    print("Division by 0")
                    return
                # print(a,b,opr[c], opr[c](a,b))
                res = opr[c](b, a)
            else:
                a = num_stack.pop()
                # print(res, c, opr[c])
                res = opr[c](a, res)

    return res


print(solution("921*-8-4+"))


def edu_solution(exp: str):
    stack = Stack()
    try:
        for char in exp:
            if char.isdigit():
                stack.push(char)
            else:
                right = stack.pop()
                left = stack.pop()
                stack.push(str(eval(left + char + right)))

        return int(float(stack.pop()))
    except ZeroDivisionError:
        print("Division by zero")
        return
    except TypeError:
        print("Invalid Sequence")
        return


print(edu_solution("921*-0/8+"))
