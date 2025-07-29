class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        d = 0
        n_d = 0
        for i in range(1,n+1):
            if i%m==0:
                d+=i
            else:
                n_d+=i
        return n_d-d