class Solution:
    def hammingWeight(self, n: int) -> int:
        str_n = str(n) 
        res = 0

        for b in str_n: 
            if b == '1': 
                res += 1 
        return res 