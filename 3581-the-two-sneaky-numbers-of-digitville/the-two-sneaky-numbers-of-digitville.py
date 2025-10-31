class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        unique = []
        res = []
        for i in nums:
            if i not in unique:
                unique.append(i)
            elif i in unique:
                res.append(i)
        return res