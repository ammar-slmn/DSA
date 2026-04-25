class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # both strings should be same length
        if len(s) != len(t): 
            return False
        
        '''
        's' : 1
        '''
        countS = {}
        countT = {} 

        for i in range(len(s)): 
            countS[s[i]] = countS.get(s[i], 0) + 1 
            countT[t[i]] = countT.get(t[i], 0) + 1 

        if countS == countT:
            return True
        return False 