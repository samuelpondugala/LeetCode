class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        ans = []
        def dfs(i):
            if i>=len(nums):
                res.append(ans.copy())
                return
            #decision to include nums[i]
            ans.append(nums[i])
            dfs(i+1)
            #decision to exclude nums[i]
            ans.pop()
            dfs(i+1)
        dfs(0)
        return res