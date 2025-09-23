class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        V1 = [int(v) for v in v1.split(".")]
        V2 = [int(v) for v in v2.split(".")]
        for i in range(max(len(V1),len(V2))):
            v1 = V1[i] if i < len(V1) else 0
            v2 = V2[i] if i < len(V2) else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0