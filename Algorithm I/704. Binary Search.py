def search(nums, target):
    # So naive approach
    # array.index, try-catch
    # try:
    #     return nums.index(target)
    # except:
    #     return -1
    
    # Binary search - Recursive approach
    
    # use 2 index : left, right
    def binary_search(left, right):
        if left <= right:
            
            # index in the middle of the array
            mid = (left+right)//2
            
            if nums[mid] < target:
                return binary_search(mid+1, right)
            elif nums[mid] > target:
                return binary_search(left, mid-1)
            else:
                return mid
            
        else:
            return -1
                
    return binary_search(0, len(nums)-1)
    
    
nums = [-1,0,3,5,9,12]
target = 8

print(search(nums, target))