class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_sum = [0]
        for i in range(len(nums)):
            prefix_sum.append(prefix_sum[-1]+nums[i])
        suffix_sum = [0]
        for i in range(len(nums)-1,0,-1):
            suffix_sum.append(suffix_sum[-1]+nums[i])
        suffix_sum = suffix_sum[::-1]
        count = 0
        for i in range(1,len(nums)):
            if prefix_sum[i] >= suffix_sum[i-1]:
                count += 1
        return count