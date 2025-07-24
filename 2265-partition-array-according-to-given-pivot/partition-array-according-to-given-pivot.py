class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller, larger, count_pivot = [], [], 0
        for n in nums:
            if n < pivot:
                smaller.append(n)
            if n > pivot:
                larger.append(n)
            if n == pivot:
                count_pivot += 1
        return smaller + [pivot]*count_pivot + larger