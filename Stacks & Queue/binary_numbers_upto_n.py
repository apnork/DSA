"""
Problem Statement:
Implement a function find_bin(n) which will generate binary numbers from 1 till n in the form of a string using a queue.


input = n  1 < n < 10000
output = List of binary numbers from 1 to n

if n = 1
    return ["1"]
c = 2
a = "0"
b = "1"
ctr = 1
res = ["1"]
for i in range(1, n+1)
    res.append( res[i] + a)
    res.append( res[i] + b)
.

"""
from queue_impl import Queue


def approach_1(n):
    if n == 1:
        return ["1"]
    a = "0"
    b = "1"
    res = ["1"]
    for i in range(1, n):
        # if len(res) - 1 >= n:
        #     break
        if n == 2:
            res.append(res[i - 1] + a)
            break
        res.append(res[i-1] + a)
        res.append(res[i-1] + b)
    return res


print(approach_1(3))


def queue_approach(n):
    res = []
    q = Queue()
    q.enqueue(1)
    for i in range(n):
        res.append(str(q.dequeue()))
        s1 = res[i] + "0"
        s2 = res[i] + "1"
        q.enqueue(int(s1))
        q.enqueue(int(s2))

    return res


print(queue_approach(0))



