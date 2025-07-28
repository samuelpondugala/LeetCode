class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        e = 0
        o = 0
        odd = False
        for i in c.values():
            if i%2==0:
                e+=i
            elif i%2!=0:
                o+=i-1
                odd = True
        if odd:
            o=o+1
        return e+o