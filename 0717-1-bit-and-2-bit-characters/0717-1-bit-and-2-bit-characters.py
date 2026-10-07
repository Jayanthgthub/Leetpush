class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i=0
        while(i<len(bits)-1):
            special = ""
            if bits[i]:
                special += str(bits[i]) +str(bits[bits[i+1]])
                i += 2
            else:
                special += str(bits[i])
                i += 1
        return i==len(bits)-1

        

        