# class Solution:
#     def findFinalValue(self, nums: List[int], original: int) -> int:
#         if original not in nums:
#             return original
#         nums.sort()
#         i = 0
#         while i<len(nums):
#             if nums[i]==original:
#                 original *= 2
#             i= i+1
#         return original
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        f = True
        while f:
            if original in nums:
                original = original * 2
            else:
                return original
        