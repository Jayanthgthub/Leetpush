class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        prefix = [0]
        for i in range(len(words)):
            prefix.append(prefix[-1] + (1 if words[i][0] in ('a','e','i','o','u') and words[i][-1] in ('a','e','i','o','u') else 0))
        ans = []
        for l,r in queries:
            ans.append(prefix[r+1]-prefix[l])
        return ans

