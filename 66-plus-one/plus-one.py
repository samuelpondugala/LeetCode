class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for d in digits:
            num = num*10 + d
        num = num+1
        num = str(num)
        nums = []
        for d in num:
            nums.append(int(d))
        return nums