class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        j=0
        prefix = ""
        while(j<len(strs[0])): 
            for i in range(1,len(strs)):
                if not(strs[i].startswith(prefix+strs[0][j])):
                    return prefix
            prefix += strs[0][j]
            j+=1
        return prefix