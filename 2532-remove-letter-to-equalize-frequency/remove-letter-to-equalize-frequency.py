class Solution:
    def equalFrequency(self, s: str) -> bool:
        c= {}
        for i in s:
            c[i] = c.get(i,0)+1
        for i in c:
            c[i] -=1
            t = [j for j in c.values() if j>0]
            if len(set(t))==1:
                return True
            c[i] +=1
        return False
