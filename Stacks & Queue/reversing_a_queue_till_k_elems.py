"""
Implement the function reverseK(queue, k) which takes a queue and a number “k” as input
and reverses the first “k” elements of the queue.

input - Queue, k
output - Queue with k elements reversed


dequeue the elements till k and add them into the stack
pop and enqueue all the elements back to the queue
As the queue is now skewed, rotate the queue size - k times
i.e. enqueue(queue.dequeue)
"""
from stack_impl import Stack
from queue_impl import Queue


def approach_1(queue: Queue, k: int):
    q_size = queue.size()
    if k > q_size or q_size == 0:
        return None
    if k < 0:
        return None

    stack = Stack()

    for i in range(k):
        stack.push(queue.dequeue())

    for i in range(k):
        queue.enqueue(stack.pop())

    # now rotate queue n - k times

    for i in range(q_size-k):
        queue.enqueue(queue.dequeue())

    return queue

