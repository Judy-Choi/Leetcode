def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """

    sub = []  
    max_length = 0

    for word in s:
        if word in sub:
            if max_length < len(sub):
                max_length = len(sub)
            i = sub.index(word)
            sub = sub[i+1 : ]
        sub.append(word)
    
    if max_length > len(sub):
        return max_length
    return len(sub)
                
# s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
s = "dvdf"

print(lengthOfLongestSubstring(s))