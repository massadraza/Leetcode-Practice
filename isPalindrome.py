class Solution:
    def isPalindrome(self, s: str) -> bool:

        pointerA = 0
        pointerB = len(s) - 1

        while pointerA < pointerB:
            while pointerA < pointerB and not s[pointerA].isalnum() :
                pointerA = pointerA + 1
            while pointerA < pointerB and not (s[pointerB].isalnum()):
                pointerB = pointerB - 1
            if s[pointerA].lower() != s[pointerB].lower():
                return False
            pointerA = pointerA + 1
            pointerB = pointerB - 1
        
        return True