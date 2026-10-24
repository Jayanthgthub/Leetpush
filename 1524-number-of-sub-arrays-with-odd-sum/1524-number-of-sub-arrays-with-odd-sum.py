class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        prefix_sum = [0]
        for i in range(len(arr)):
            prefix_sum.append(prefix_sum[-1]+arr[i])
        total = 0
        even,odd=0,0
        for i in range(len(prefix_sum)):
            if prefix_sum[i]%2==0:
                even += 1
            else:
                odd += 1
        return (even*odd)%(10**9 + 7)
        