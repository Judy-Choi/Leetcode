def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    # Convert string to List to access charactor 1 by 1
    s = list(s)
    # Make Q and input if the word doesn't exists in the Q
    queue = []
    
    max_str_length = 0

    # Input charactor to Q
    for char in s:
        if char in queue:
            # if len(queue) > max_str_length:
            #     max_str_length = len(queue)
            index = queue.index(char)
            queue = queue[index + 1 : ]
        queue.append(char)
        max_str_length = max(max_str_length, len(queue))
                
    return max_str_length
                
# s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
s = "dvdf"

print(lengthOfLongestSubstring(s))