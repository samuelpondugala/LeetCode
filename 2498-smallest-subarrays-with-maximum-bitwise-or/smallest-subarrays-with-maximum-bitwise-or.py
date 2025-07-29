class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        rightmost = [0] * 30  # Track farthest index where bit is set
        res = [0] * n

        for i in range(n - 1, -1, -1):
            for b in range(30):  # Loop over all 30 bit positions
                if nums[i] & (1 << b):
                    rightmost[b] = i  # Update where this bit is last seen

            # The max index needed to preserve current OR
            max_len = i
            for j in range(30):
                max_len = max(max_len, rightmost[j])

            res[i] = max_len - i + 1  # Length of subarray

        return res
