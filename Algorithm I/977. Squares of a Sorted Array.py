def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    # 1. Basic python
    # for i, n in enumerate(nums):
    #     nums[i] = n*n

    # nums.sort()
    # return nums

    # 2. Just 1 line
    return sorted([n**2 for n in nums])
    
nums = [-4,-1,0,3,10]

print(sortedSquares(nums))