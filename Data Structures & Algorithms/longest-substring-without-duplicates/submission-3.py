class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        idxMap = defaultdict(int)
        l = 0
        length = 0

        for r in range(len(s)): 
            if s[r] in idxMap: 
                l = max(l, idxMap[s[r]] + 1)
            idxMap[s[r]] = r
            length = max(length, r - l + 1) 
        return length
