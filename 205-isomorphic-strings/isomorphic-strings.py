# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         f1 = {}
#         b1 = {}
#         f2 = {}
#         b2 = {}
#         if len(s)==len(t):
#             for i in range(len(s)):
#                 f1[s[i]] = t[i]
#             for i in range(len(s)-1, -1, -1):
#                 b1[s[i]] = t[i]
#             for i in range(len(s)):
#                 f2[t[i]] = s[i]
#             for i in range(len(s)-1, -1, -1):
#                 b2[t[i]] = s[i]
#         return (f1==b1 and f2==b2) and (len(set(s))==len(set(t)))
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapping={}
        used=set()
        for ch1,ch2 in zip(s,t):
            if ch1 in mapping:
                if mapping[ch1]!=ch2:
                    return False
            else:
                if ch2 in used:
                    return False
                mapping[ch1]=ch2
                used.add(ch2)
        return True