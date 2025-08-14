class Solution:
    def largestGoodInteger(self, s: str) -> str:
        res = ""
        for i in range(len(s) - 2):
            if s[i] == s[i+1] == s[i+2]:
                if res == "" or s[i:i+3] > res:
                    res = s[i:i+3]
        return res