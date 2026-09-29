class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        s = sum(nums)
        s1 = sum(range(0,len(nums)+1))
        return s1-s