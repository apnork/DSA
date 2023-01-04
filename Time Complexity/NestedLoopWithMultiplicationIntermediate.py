# code snippet

n = 10  # can be anything, this is just an example
sum = 0
pie = 3.14
for var in range(1, n, 3):
    j = 1
    print(pie)
    while j < n:
        sum += 1
        j *= 3
print(sum)  # O(1)


"""
outer for loop:
rtc = n/k => n/3

inner while loop:
log_3(n)

n/3 * log_3(n)

Simplifying =>

TC = n*log_3(n)

"""