class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t1 = sorted(t)
        s1 = sorted(s)
        for i in range(len(t1)-1):
            if t1[i]!=s1[i]:
                return t1[i]
        return t1[len(t)-1]