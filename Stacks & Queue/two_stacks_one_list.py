class TwoStacks:
    # Initialize the two stacks here
    def __init__(self, size):
        self.stack_list = [None] * size

    # Insert Value in First Stack
    def push1(self, value):
        self.stack_list.insert(0, value)
        return True

    # Insert Value in Second Stack
    def push2(self, value):
        self.stack_list[-1] = value
        return True

    # Return and remove top Value from First Stack
    def pop1(self):
        if len(self.stack_list) == 0:
            return False
        return self.stack_list.pop(0)

    # Return and remove top Value from Second Stack
    def pop2(self):
        if len(self.stack_list) == 0:
            return False
        return self.stack_list.pop()


class TwoStacksSolution:
    # Initialize the two stacks here
    def __init__(self, size):
        self.stack_list = [None] * size
        self.size = size
        self.top1 = -1
        self.top2 = size

    # Insert Value in First Stack
    def push1(self, value):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.stack_list[self.top1] = value
        else:
            print("Stack overflow")
            exit(1)

    # Insert Value in Second Stack
    def push2(self, value):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.stack_list[self.top2] = value
        else:
            print("Stack Overflow")
            exit(1)

    # Return and remove top Value from First Stack
    def pop1(self):
        if self.top1 >= 0:
            pop_elem = self.stack_list[self.top1]
            self.top1 -= 1
            return pop_elem
        else:
            print("Stack Underflow")
            exit(1)

    # Return and remove top Value from Second Stack
    def pop2(self):
        if self.top2 <= self.size:
            pop_elem = self.stack_list[self.top2]
            self.top2 += 1
            return pop_elem
        else:
            print("Stack Underflow")
            exit(1)


if __name__ == "__main__" :
    stack = TwoStacksSolution(10)
    stack.push1(20)
    print(stack.pop1())
    stack.push1(100)
    print(stack.pop2())
