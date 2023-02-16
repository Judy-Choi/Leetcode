# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n==1): return 1

        # binary_search approach
        # If I use quick sort, I think it can be more faster.
        def binary_search(start, end):
            while start < end:
                mid = (start + end) // 2

                if (isBadVersion(mid)):
                    return binary_search(start, mid)
                else:
                    return binary_search(mid+1, end)
            return start

        return binary_search(1, n)