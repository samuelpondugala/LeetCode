class Solution:
    def finalValueAfterOperations(self, l: List[str]) -> int:
        res = 0
        for i in l:
            if i == "++X" or i=="X++":
                res+=1
            elif i == "--X" or i=="X--":
                res-=1
        return res
