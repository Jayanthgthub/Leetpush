class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0 or n&(n-1)!=0:
            return False
        count = 0
        while(n!=1):
            n = n>>1
            count += 1
            
        if (count)%2==0:
            return True
        else:
            return False

