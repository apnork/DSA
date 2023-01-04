# code snippet

n = 10  # Can be anything
sum = 0
pie = 3.14
var = 1
while var < n:
    print(pie)
    for j in range(var):
        sum += 1
    var *= 2
print(sum)


"""
TC = O(nlogn)

For loops that have multiplication on the loop variable this will put the running time in the logarithmic range.
So RT = logk(n) where n is the input size and k is the constant multiplier of the loop variable.

for outer loop:
RT = log2(n)
for inner loop:
n
total RT = log2(n) * n
"""

"""
The answer above is incorrect, the correct answer is O(n)

So the total running time of the outer loop is
comparisons in while+printing pie+doubling var

Total RT of outer loop is 4log2(n) + 1

For inner loop
Since var changes in the powers of 2 everytime , the time complexity would become 2^(runtime of outer loop)

So,
 RTC = 2 ^ (log_2(n))
    = O(n)
"""