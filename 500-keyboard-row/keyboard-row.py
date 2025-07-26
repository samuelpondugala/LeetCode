class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = "qwertyuiopQWERTYUIOP"
        second = "ASDFGHJKLasdfghjkl"
        third = "zxcvbnmZXCVBNM"
        res = []
        for i in words:
            if i[0] in first:
                if all(j in first for j in list(i)):
                    res.append(i)
            if i[0] in second:
                if all(j in second for j in list(i)):
                    res.append(i)
            if i[0] in third:
                if all(j in third for j in list(i)):
                    res.append(i)
        return res
            
        