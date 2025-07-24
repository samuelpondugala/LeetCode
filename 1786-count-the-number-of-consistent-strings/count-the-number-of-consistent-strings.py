class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # c = 0
        # for i in range(len(words)):
        #     present = True
        #     for j in range(len(words[i])):
        #         if words[i][j] not in allowed:
        #             present = False
        #     if present:
        #         c+=1
        # return c
        # c1=0
        # for i in words:
        #     if set(i).issubset(set(allowed)):
        #         c1+=1
        # return c1
        allowed_set = set(allowed) 
        res = 0 
        for word in words: 
            for char in word: 
                flag = True 
                if char not in allowed_set: 
                    flag = False 
                    break 
            if flag: 
                res += 1 
            

        return res 