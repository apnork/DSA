class Stack:
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0

    def is_empty(self) -> bool:
        if self.stack_size == 0:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            return -1
        return self.stack_list[-1]

    def size(self):
        return self.stack_size

    def push(self, data):
        self.stack_list.append(data)
        self.stack_size += 1
        return True

    def pop(self):
        if self.is_empty():
            return -1
        temp = self.stack_list.pop()
        self.stack_size -= 1
        return temp

    def print_stack(self):
        stacc = "["
        for i in range(self.stack_size - 1):
            stacc = stacc + str(self.stack_list[i]) + ","

        stacc = stacc + str(self.stack_list[-1]) + "]"
        print(stacc)
        return True
