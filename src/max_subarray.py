nums = [-2,1,-3,4,-1,2,1,-5,4]

def max_subarray(A):
    max_ending_here = max_so_far = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)

    if max_so_far > 0:
        return max_so_far
    else:
        return max(A)


print(max_subarray(nums))




