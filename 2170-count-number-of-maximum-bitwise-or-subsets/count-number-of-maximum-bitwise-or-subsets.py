class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
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
        summ = []
        def xor(res):
            for num in res:
                xor_sum = 0
                for i in num:
                    xor_sum |= i  # Bitwise XOR operation
                summ.append(xor_sum)
        xor(res)
        maxx = max(summ)
        return summ.count(maxx)