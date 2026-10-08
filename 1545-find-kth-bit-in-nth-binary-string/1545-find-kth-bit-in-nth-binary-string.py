class Solution(object):
    # def reverse(self,prev):
    #     rev_prev = ""
    #     while(prev!=""):
    #         if prev[-1]=="1":
    #             rev_prev += str(0)
    #         else:
    #             rev_prev += str(1)
    #         prev = prev[:-1]
    #     return rev_prev
            


    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # previous="0"
        # present= ""
        # for i in range(1,n+1):
        #     present += previous + "1" + self.reverse(previous)
        #     previous = present
        #     present = ""
        # return previous[k-1]
        sn = "0"
        for i in range(n):
            invert =""
            for j in sn:
                if j == "1":
                    invert+= "0"
                else:
                    invert += "1"
            sn += "1"+invert[::-1]
        return sn[k-1]
        