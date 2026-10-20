class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        # maxi = 0
        # for i in range(1,len(s)):
        #     left = s[:i]
        #     right = s[i:]
        #     maxi = max(left.count("0"),right.count("1"))
        # return maxi
        # if len(s)==2:
        #     return ((1 if s[0]=="0" else 0) + (1 if s[1]=="1" else 0))
        prefix_sum = [0]
        for i in range(1,len(s)):
            prefix_sum.append(prefix_sum[-1] + (1 if s[i-1]=="0" else 0))
        suffix_sum = [0]
        for i in range(len(s)-2,-1,-1): 
            suffix_sum.append(suffix_sum[-1]+ (1 if s[i+1]=="1" else 0))
        suffix_sum = suffix_sum[::-1]
        score = 0
        for i in range(1,len(s)):
            score = max(score,prefix_sum[i]+suffix_sum[i-1])
        return score

        