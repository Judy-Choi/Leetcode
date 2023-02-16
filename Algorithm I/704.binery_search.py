def search(nums, target):
    # So naive approach
    # array.index, try-catch
    try:
        return nums.index(target)
    except:
        return -1
    
    # Binary Search

    
    
nums = [-1,0,3,5,9,12]
target = 8

print(search(nums, target))