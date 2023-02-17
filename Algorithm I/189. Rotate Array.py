def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    
    n = len(nums)
    k = k % len(nums)
    # nums[:] 로 넣기!!!!!
    # 파이썬의 notation (: 쓰는 거) 을 사용하여 슬라이싱을 할 경우
    # 새로운 배열로 deepcopy (데이터 자체를 통째로 복사, 독립 메모리 보유).
    # in-place 방식이 아님.
    # : 안 쓰면 shallow copy 가 일어나서 leetcode 플랫폼에서는 문제가 되는 듯. (vscode 정상동작.)
    nums[:] = nums[n-k:] + nums[:n-k]

    return nums

nums = [1,2,3,4,5,6,7]
k = 3

# nums = [-1,-100,3,99]
# k = 2

print(rotate(nums, k))