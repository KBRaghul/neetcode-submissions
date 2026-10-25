class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sets = set()
        maxlen = 0

        for r in range(len(s)):
            while s[r] in sets:
                sets.remove(s[l])
                l += 1
            sets.add(s[r])
            maxlen = max(maxlen, r-l+1)

        return maxlen
            
            

        