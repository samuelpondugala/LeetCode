class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = Counter(nums)
        pairs = 0
        for i in c.values():
            pairs+=(i*(i-1))//2
        return pairs