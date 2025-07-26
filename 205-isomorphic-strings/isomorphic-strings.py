class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        f1 = {}
        b1 = {}
        f2 = {}
        b2 = {}
        if len(s)==len(t):
            for i in range(len(s)):
                f1[s[i]] = t[i]
            for i in range(len(s)-1, -1, -1):
                b1[s[i]] = t[i]
            for i in range(len(s)):
                f2[t[i]] = s[i]
            for i in range(len(s)-1, -1, -1):
                b2[t[i]] = s[i]
        return (f1==b1 and f2==b2) and (len(set(s))==len(set(t)))
            