
def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    
    # def binary_search(left, right):
    #     if left <= right:
            
    #         # index in the middle of the array
    #         mid = (left+right)//2
            
    #         if nums[mid] < target:
    #             return binary_search(mid+1, right)
    #         elif nums[mid] > target:
    #             return binary_search(left, mid-1)
    #         else:
    #             return mid
            
    #     else:
    #         return left
                
    # return binary_search(0, len(nums)-1)
    
    # While-loop approach
    left=0
    right=len(nums)-1
    
    while left<=right:
        mid=(left+right)//2
        if nums[mid]<target: # Search to right 
            left=mid+1
        elif nums[mid]>target: # Search to left
            right=mid-1
        else: # Correct
            return mid
    # Incorrect
    return left 

# nums = [1,3,5,6]
# target = 5
# nums = [1,3,5,6]
# target = 2
nums = [1,3,5,6]
target = 7

print(searchInsert(nums, target))