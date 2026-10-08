class Solution(object):
    def minChanges(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        n1 = ""
        k1 = ""
        while(n!=0):
            n1 += str(n&1)
            n>>=1
        while(k!=0):
            k1 += str(k&1)
            k>>=1
        if len(n1)>len(k1):
            k1 += "0"*(abs(len(n1)-len(k1)))
        else:
            n1 += "0"*(abs(len(n1)-len(k1)))
        count = 0
        for i in range(max(len(n1),len(k1))):
            if n1[i]!=k1[i]:
                if n1[i] == "0":
                    return -1
                else:
                    count += 1
        return count



        