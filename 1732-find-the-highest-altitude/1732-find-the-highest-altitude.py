class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        prefix_sum = [0]
        maxi = prefix_sum[0]
        for i in range(len(gain)):
            prefix_sum.append(prefix_sum[-1] + gain[i])
            maxi = max(maxi,prefix_sum[-1])
        return maxi

        