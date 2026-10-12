class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num==0:
            return 1
        bits = ""
        while(num!=0):
            bit = num&1
            if bit == 0:
                bit = 1
            else:
                bit = 0
            bits += str(bit)
            num>>=1
        n1 = 0
        for i in range(len(bits)):
            n1 += (2 ** i)*(int(bits[i]))
        return n1