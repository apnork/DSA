# code snippet

n = 10  # n can be anything, this is just an example
sum = 0
pie = 3.14
for var in range(n, 1, -3):
    print(pie)
    for j in range(n, 0, -1):
        sum += 1

print(sum)

"""
TC = O(n2)

Since the loop variable for both outer and inner loop does not effect the execution of the loops itself. These variables
affect only non important thing inside the loop.

NOTE: The TC for a step for loop is calculated as n/k where is n is the size of the loop and k is the step.
"""