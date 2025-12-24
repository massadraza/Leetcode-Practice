class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        p = 0
        q = len(s1)

        s1Sorted = "".join(sorted(s1))

        while q <= len(s2):
            tempStr = s2[p:q]
            tempSorted = "".join(sorted(tempStr))
            if s1Sorted == tempSorted:
                return True
            else:
                p += 1
                q += 1

        return False