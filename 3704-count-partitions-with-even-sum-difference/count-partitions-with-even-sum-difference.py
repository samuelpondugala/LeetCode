class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        c =0
        for k in range(len(nums)-1):
            diff = sum(nums[:k+1])-sum(nums[k+1:])
            if(diff%2==0):
                c+=1
        return c