class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        L = []
        for i in range(n+1):
            count = 0
            n=i
            while(n!=0):
                bit=n&1
                n>>=1
                if bit==1:
                    count += 1
            L.append(count)
        return L
                

        