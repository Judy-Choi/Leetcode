def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """

    # Array
    # Runtime 27 ms, Mrmory 14.6 MB    
    subwords = s.split(' ')
    arr = []

    for subword in subwords:
        reversed = list(subword)
        reversed.reverse()
        arr.append(''.join(reversed))

    return ' '.join(arr)
    
    # String
    # Runtime 54 ms, Memory 14.7 MB
    # subwords = s.split(' ')
    # str = ""

    # for subword in subwords:
    #     reversed = list(subword)
    #     reversed.reverse()
    #     str += ''.join(reversed) + ' '

    # return str[:-1]
    
    # Simplest Python Logic using Split() Function
    # s_list = s.split()
    # st = ""
    # for i in s_list:
    #     st += i[::-1] + " "
    
    # st = st[:-1]
    
    # return st

s = "Let's take LeetCode contest"

print(reverseWords(s))