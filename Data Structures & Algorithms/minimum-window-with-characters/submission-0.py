class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countS, countT = {}, {}

        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        have, l = 0, 0
        need = len(countT)
        res = [-1, -1]
        res_len = float("infinity")

        for r in range(len(s)):
            c = s[r]
            countS[c] = 1 + countS.get(c, 0)

            if c in countT and countS[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < res_len:
                    res = [l, r]
                    res_len = (r-l+1)
                
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if res_len != float("infinity") else ""
