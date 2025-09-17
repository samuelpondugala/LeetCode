class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        counts=0
        i=0
        max_1=0
        for j in range(len(nums)):
            if nums[j]==0:
                counts+=1
            while counts>1:
                if nums[i]==0:
                    counts-=1
                i+=1
            max_1=max(max_1,j-i)
        return max_1