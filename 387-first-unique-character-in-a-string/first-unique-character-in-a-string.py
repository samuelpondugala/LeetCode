
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for ch in s:
            if c[ch] == 1:
                return s.index(ch)
        else:
            return -1