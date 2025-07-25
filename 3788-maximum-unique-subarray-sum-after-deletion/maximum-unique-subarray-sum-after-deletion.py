class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # if len(set(nums))==1:
        #     return list(set(nums))[0]
        # if all(i<0 for i in nums):
        #     return max(nums)
        # res = []
        # for i in nums:
        #     if i not in res and i>=0:
        #         res.append(i)
        # return sum(res)
        if max(nums)<0 :
            return max(nums)
        else:
            result=0
            nums=set(nums)
            for i in nums:
                if i>=0:
                    result+=i
            return result