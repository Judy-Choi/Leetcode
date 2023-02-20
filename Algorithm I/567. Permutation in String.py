def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    
    # Time Out!!!!
    # s1 = list(s1)
    # s2 = list(s2)
    
    # s1.sort()
    
    # for i, s in enumerate(s2):
    #     if s in s1:
    #         s2_sub = s2[i : i + len(s1)]
    #         s2_sub.sort()
            
    #         if s1 == s2_sub:
    #             return True
    # return False
    
    # Counter can be a simple solution
    # ex) >>> Counter("hello world")
    # Counter({'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
    
    from collections import Counter
    
    c1 = Counter(s1)
    c2 = Counter()
    W = len(s1)
    
    for i,c in enumerate(s2):
        # input 'word' : 1 to Counter c2
        c2[c] += 1
        
        # if window length > s1 length :
        # Let 0 first input of the window (sliding window 1 step left -> right)
        if i >= W:
            c2[s2[i-W]] -= 1
        
        if c1 == c2: 
            return True
    
    return False

s1 = "ab"
s2 = "eidbaooo"

# s1 = "ab"
# s2 = "eidboaoo"

# s1 = "dinitrophenylhydrazine"
# s2 = "acetylphenylhydrazine"

# s1 = "adc"
# s2 = "dcda"

# s1 = "abc"
# s2 = "bbbca"

print(checkInclusion(s1, s2))