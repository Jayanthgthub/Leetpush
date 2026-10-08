class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        # n = ""
        # while(start!=0):
        #     n += str(start&1)
        #     start>>=1
        # k = ""
        # while(goal!=0):
        #     k += str(goal&1)
        #     goal >>=1
        # if len(n)>len(k):
        #     k += "0"*(abs(len(n)-len(k)))
        #     maxi = len(n)
        # else:
        #     n += "0"*(abs(len(n)-len(k)))
        #     maxi = len(k)
        # for i in range(maxi):
        #     if n[i]
        changes = start ^ goal
        count = 0
        while(changes!=0):
            count += 1
            changes = changes & (changes-1)
        return count
        