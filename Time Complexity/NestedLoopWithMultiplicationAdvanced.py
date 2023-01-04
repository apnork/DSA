# code snippet

n = 10  # can be anything
sum = 0
pie = 3.14
for i in range(n):
    j = 1
    while j < i:
        sum += 1
        j *= 2
    print(sum)

"""
rtc outer loop:
n

rtc inner loop:
log_2(n)

TC = nlogn
"""
