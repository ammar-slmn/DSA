class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False 

        countS = {}
        countT = {}

        for i in range(len(s)):     
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        print(countS)
        print(countT)

        if countS == countT: 
            return True
        return False 