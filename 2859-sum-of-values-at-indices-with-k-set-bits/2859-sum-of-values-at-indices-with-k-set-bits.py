class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = 0
        for i in range(len(nums)):
            n = i
            count = 0
            while(n!=0):
                count += 1
                n = n & (n-1)
            if count == k:
                sum += nums[i]
        return sum


        