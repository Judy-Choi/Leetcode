class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        # Thx to Python
        return s.reverse()

        # Use 2 pointers
        # start = 0
        # end = len(s)-1

        # while(start < end):
        #     tmp = s[start]
        #     s[start] = s[end]
        #     s[end] = tmp
        #     start += 1
        #     end -= 1
        # return s