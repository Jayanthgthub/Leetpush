class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # n = x
        # x1 = []
        # while(n!=0):
        #     x1.append(n&1)
        #     n >>= 1
        # n = y
        # y1 = []
        # while(n!=0):
        #     y1.append(n&1)
        #     n>>=1
        # l_x1,l_y1 = len(x1),len(y1)
        # for i in range(abs(l_x1-l_y1)):
        #     if l_x1>l_y1:
        #         y1.append(0)
        #     else:
        #         x1.append(0)

        # count = 0
        # for i in range(len(x1)):
        #     if x1[i]!=y1[i]:
        #         count += 1
        # return count
        c = x^y
        n= c
        count = 0
        while(n!=0):
            if n&1==1:
                count += 1
            n>>=1
        return count
        