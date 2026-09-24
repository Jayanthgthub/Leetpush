class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            nums[i] = str(nums[i])
            sum = 0
            for j in nums[i]:
                sum += int(j)
            if sum==i:
                return i 
        return -1
                
        