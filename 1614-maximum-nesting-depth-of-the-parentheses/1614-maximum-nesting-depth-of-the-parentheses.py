class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        max = 0
        count = 0
        para_count = 0
        for i in s:
            if i =="(":
                count += 1
                if count>max:
                    max = count
            elif i==")":
                count -=1
        return max

                