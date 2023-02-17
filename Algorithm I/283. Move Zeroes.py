class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # Memory wasted approach
        arr = []
        zeros = []
        
        for i, n in enumerate(nums):
            if n != 0:
                arr.append(n)
            else:
                zeros.append(0)

        nums[:] = arr + zeros

        return nums