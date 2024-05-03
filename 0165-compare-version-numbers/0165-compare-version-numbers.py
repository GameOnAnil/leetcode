class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split('.')
        for i in range(max(len(v1),len(v2))):
            a = 0
            b = 0
            if i < len(v1):
                a = int(v1[i])
            if i < len(v2):
                b = int(v2[i])
            if a < b:
                return -1
            elif a >b:
                return 1
        return 0

        