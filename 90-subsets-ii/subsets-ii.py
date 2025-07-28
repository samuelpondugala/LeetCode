class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        ans = []
        def dfs(i):
            if i>=len(nums):
                res.append(ans.copy())
                return
            ans.append(nums[i])
            dfs(i+1)
            ans.pop()
            idx = i+1
            while idx<len(nums) and nums[idx]==nums[idx-1]:
                idx+=1
            dfs(idx)
        dfs(0)
        return res

