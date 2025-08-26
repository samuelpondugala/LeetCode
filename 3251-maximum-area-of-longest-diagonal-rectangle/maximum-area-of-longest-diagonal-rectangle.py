import math as m
class Solution:
    def areaOfMaxDiagonal(self, l: List[List[int]]) -> int:
        res = []
        for i in range(len(l)):
            dia = m.sqrt(l[i][0]*l[i][0] + l[i][1]*l[i][1])
            res.append(dia)
        indices = []
        target_element = max(res)
        for index, element in enumerate(res):
            if element == target_element:
                indices.append(index)
        prods = [m.prod(l[i]) for i in indices]
        return max(prods)