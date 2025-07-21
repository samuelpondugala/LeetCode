class Solution:
    def makeFancyString(self, s: str) -> str:
        res = s[0]
        l = s[0]
        c = 1
        for i in range(1, len(s)):
            if s[i] != l:
                l = s[i]
                c = 0
            c += 1
            if c > 2:
                continue
            res += s[i]
        return res
