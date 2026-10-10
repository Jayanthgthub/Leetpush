class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # count = 0
        # while n:
        #     if n&1:
        #         count += 1
        #     n>>=1
        # return count==1 
        return n>0 and n&(n-1)==0
        