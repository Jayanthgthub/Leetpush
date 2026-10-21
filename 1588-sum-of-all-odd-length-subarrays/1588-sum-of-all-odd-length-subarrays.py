class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        prefix_sum = [0]
        for i in range(len(arr)):
            prefix_sum.append(prefix_sum[-1]+arr[i])
            sum=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if (j-i+1)%2!=0:
                    sum += prefix_sum[j+1] - prefix_sum[i]
        sum += prefix_sum[-1]
        return sum
