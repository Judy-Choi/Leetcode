def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """

    # for i, n in enumerate(numbers):
    #     sub = target - n
    #     if sub in numbers[i+1:]:
    #         return [i+1, numbers[i+1:].index(sub) + i + 2]
    
    # Timeout Occur!
    # numbers = [0,0,0,0,0,0,0,0....]
    
    # Too many elements -> Solution : dictionary!
    # The best way I tried.
    dic = {}
    for i, n in enumerate(numbers):
        sub = target - n
        if sub in dic:
            return [dic[sub]+1, i+1]
        else:
            dic[n] = i
    
    # But still too late...
    # Let's try pointer
    # Thanks to already sorted list :)
    # ...Still too late && even more memory -_-;;
    # start = 0
    # end = len(numbers) - 1
    
    # while start < end:
    #     sum = numbers[start] + numbers[end]
    #     if sum == target:
    #         return [start+1, end+1]
    #     elif sum < target:
    #         start += 1
    #     else:
    #         end -= 1

# Test Case        
# numbers = [0,0,3,4]
# target = 0

# numbers = [2,7,11,15]
# target = 9

numbers = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,3,4,9,9,9,9,9,9,9,9,9,9,9,9,]
target = 5

print(twoSum(numbers, target))