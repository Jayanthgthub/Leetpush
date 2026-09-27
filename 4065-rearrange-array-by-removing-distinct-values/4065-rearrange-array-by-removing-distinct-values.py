class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        while nums:
            unique = sorted(list(set(nums)))
            ans.extend(unique)
            for i in unique:
                nums.remove(i)
        return ans