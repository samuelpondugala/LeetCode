class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        ans = 0
        for i in range(len(fruits)):
            flag = False
            for j in range(len(baskets)):
                if fruits[i]<=baskets[j]:
                    baskets[j] = 0
                    flag = True
                    break
            if not flag:
                ans+=1
        return ans
