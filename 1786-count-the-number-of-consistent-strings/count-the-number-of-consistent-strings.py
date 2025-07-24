class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c1=0
        for i in words:
            if set(i).issubset(set(allowed)):
                c1+=1
        return c1
        