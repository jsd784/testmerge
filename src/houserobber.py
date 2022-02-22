nums = [2,7,1,3,1]

def houseRob(A):

    amt1 = amt2 = 0

    for i in range(len(A)):
        if i % 2 == 0:
            amt1 = amt1 + A[i]
        else:
            amt2 = amt2 + A[i]

    return max(amt1,amt2)


print(houseRob(nums))