class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        b = set(bannedWords)
        c = 0
        for i in message:
            if i in b:
                c += 1
                if c > 1:
                    return True
        return False