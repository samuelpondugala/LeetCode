class Solution:
    def defangIPaddr(self, s: str) -> str:
        res = ""
        for i in s:
            if i == ".":
                res+='[.]'
            else:
                res+=i
        return res