class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # res = []
        # i = 0
        # j = n
        # while i<n and j<len(nums):
        #     res.append(nums[i])
        #     res.append(nums[j])
        #     i+=1
        #     j+=1
        # while i<n:
        #     res.append(nums[i])
        #     i+=1
        # while j<len(nums):
        #     res.append(nums[j])
        #     j+=1
        # return res
        ans = []
        for i in range(n):
            ans += [nums[i]] 
            ans += [nums[i+n]]
        return ans