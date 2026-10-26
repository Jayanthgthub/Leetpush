class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sums = [0]
        dict_a={0:1}
        count = 0
        for i in range(len(nums)):
            prefix_sums.append(prefix_sums[-1]+nums[i])
            rem = prefix_sums[i+1]%k
            if rem in dict_a.keys():
                count += dict_a[rem]
                dict_a[rem] += 1
            else:
                dict_a[rem] = 1
        return count
            
