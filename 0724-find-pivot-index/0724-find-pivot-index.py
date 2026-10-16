class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_sum =[0]
        suffix_sum = [0]
        j = len(nums)-1
        for i in range(len(nums)-1):
            prefix_sum.append(prefix_sum[-1]+nums[i])
            suffix_sum.append(suffix_sum[-1]+nums[j])
            j -= 1
        suffix_sum = suffix_sum[::-1]
        for i in range(len(prefix_sum)):
            if prefix_sum[i]==suffix_sum[i]:
                return i
        return -1
