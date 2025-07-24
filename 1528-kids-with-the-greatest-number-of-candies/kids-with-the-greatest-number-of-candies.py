class Solution:
    def kidsWithCandies(self, candies: List[int], e: int) -> List[bool]:
        n = len(candies)
        res = [False]*n
        m = max(candies)
        for i in range(n):
            if (candies[i]+e)>=m:
                res[i] = True
        return res