class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num =0
        i=0
        value = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        # while(i<len(s)):
        #     if i<len(s)-1:
        #         if s[i]=="I":
        #             if s[i+1] =="V":
        #                 num += 4
        #                 i+=2
        #                 continue
        #             elif s[i+1] == "X":
        #                 num += 9
        #                 i+=2
        #                 continue
        #         elif s[i] == "X":
        #             if s[i+1] == "L":
        #                 num += 40
        #                 i+=2
        #                 continue 
        #             elif s[i+1]=="C":
        #                 num += 90
        #                 i+=2
        #                 continue 
        #         elif s[i] == "C":
        #             if s[i+1] == "D":
        #                 num += 400 
        #                 i+=2
        #                 continue
        #             elif s[i+1]=="M":
        #                 num += 900
        #                 i+=2
        #                 continue
        #     num += roman[s[i]]
        #     i += 1 
        # return num
        n = s
        result =0 
        for i in range (len(n)):
            if i+1<len(n) and value[n[i]]<value[n[i+1]]:
                result-=value[n[i]]
            else:
                result+=value[n[i]]
        return result

