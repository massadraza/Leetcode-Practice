class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            result = result + str(len(i)) + "-" + i
        
        return result

    def decode(self, s: str) -> List[str]:
        res = []
        pointer = 0
        while pointer < len(s):
            j = pointer
            while s[j] != "-":
                j = j + 1
            length = int(s[pointer:j])
            res.append(s[j + 1: j + 1 + length])
            pointer = j + 1 + length
        
        return res



