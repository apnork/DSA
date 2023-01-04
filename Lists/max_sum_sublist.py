# problem statement

# This is a dynamic programming question, and it can be solved Kadane's Algorithm

"""
[-1,4,0,-1,6,2,-2,5,8,0,-1]

current_max = A[0]
global_max = A[0]
for i = 1 -> size of A
    if current_max is less than 0
        then current_max = A[i]
    otherwise
        current_max = current_max + A[i]
    if global_max is less than current_max
        then global_max = current_max
"""


def find_max_sum_sublist(lst):
    if len(lst) < 1:
        return 0

    curr_max = lst[0]
    global_max = lst[0]
    length_array = len(lst)
    for i in range(1, length_array):
        if curr_max < 0:
            curr_max = lst[i]
        else:
            curr_max += lst[i]
        if global_max < curr_max:
            global_max = curr_max

    return global_max


lst = [-4, 2, -5, 1, 2, 3, 6, -5, 1]
print("Sum of largest subarray: ", find_max_sum_sublist(lst))
