class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        prefix =[0]
        for i in nums:
            prefix.append(prefix[-1]+i)
        avgs = []
        for i in range(len(nums)):
            if i<k or i+k>=len(nums):
                avgs.append(-1)
            else:
                total = prefix[i+k+1] - prefix[i-k]
                avgs.append((total)//(2*k+1))
        return avgs
        