class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_a = dict()
        for i in nums:
            if i not in dict_a:
                dict_a[i]=1 
            else:
                dict_a[i]+= 1
        for key in dict_a.keys():
            if dict_a[key]>len(nums)//2:
                return key

        # return dict_a.keys()[1]

        