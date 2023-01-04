# code snippet

n = 10  # n can be anything, this is just an example
sum = 0
pie = 3.14

for var in range(1, n, 3):
    print(pie)
    for j in range(1, n, 2):
        sum += 1
        print(sum)

"""
The time complexity for this is O(n2) as the stepper in the outer loop does not effect the inner loops range or any 
constant operation that was performed inside of it.

TC = O(n2)
"""