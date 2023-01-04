# code snippet

n = 10  # can be anything
sum = 0
pie = 3.14
j = 1
for var in range(n):
    while j < var:
        sum += 1
        j *= 2
    print(sum)

"""
rtc outer loop:
n

rtc inner loop:
    Inner loops depends on the value of `var` which keeps on increasing with the size of `n`
    Inner loops also has multiplies the loop variable with 2 everytime it runs, thus putting it on a log based rtc
This will run for -> 
    comparison + sum + access `j` + multiply `j` by 2
    
"""