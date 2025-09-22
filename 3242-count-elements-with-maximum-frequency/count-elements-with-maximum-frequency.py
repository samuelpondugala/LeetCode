class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = sorted(Counter(nums).items(), key = lambda x:x[1], reverse=True)
        max_c = max(c,key=lambda x:x[1])[1]
        if len(nums)==len(c):
            return len(nums)
        count = 0
        for k,v in c:
            if v==max_c:
                count+=v
        return count
                
        
