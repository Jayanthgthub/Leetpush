class Solution(object):
    def evenOddBit(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        L=[0,0]
        k=0
        while(k<n.bit_length()):
            if n&(1<<k):
                if(k%2==0):
                    L[0]+=1
                else:
                    L[1]+=1
            k+=1
        return L
    

        