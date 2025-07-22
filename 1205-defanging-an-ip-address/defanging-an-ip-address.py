class Solution:
    def defangIPaddr(self, s: str) -> str:
        return s.replace(".","[.]")