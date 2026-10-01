class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # word = ""
        # L = []
        # for i in range(len(s)):
        #     if s[i]!=" ":
        #         word += s[i]
        #         if i==len(s)-1 and word!="":
        #             L.append(word)
        #     else:
        #         if word!="":
        #             L.append(word)
        #         word = ""
        # return len(L[-1])

        s = s.strip()
        s = s.split()
        return len(s[-1])