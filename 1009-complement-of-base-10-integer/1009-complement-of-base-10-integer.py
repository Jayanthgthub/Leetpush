class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        bits = ""
        while(n!=0):
            bit = n&1
            if bit == 0:
                bit = 1
            else:
                bit = 0
            bits += str(bit)
            n>>=1
        n1 = 0
        for i in range(len(bits)):
            n1 += (2 ** i)*(int(bits[i]))
        return n1