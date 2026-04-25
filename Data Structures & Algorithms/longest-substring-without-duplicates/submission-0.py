class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        left = 0
        res = 0

        for i in range(len(s)):
            if s[i] in map:
                left = max(map[s[i]] + 1, left)
            map[s[i]] = i
            res = max(res, i - left + 1)
        return res