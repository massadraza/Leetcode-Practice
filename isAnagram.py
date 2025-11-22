class Solution:

    # Created by: Massad Raza
    
    def isAnagram(self, s: str, t: str) -> bool:
        letters = dict()
        lettersTwo = dict()

        if len(s) != len(t):
            return False

        
        for i in s:
            if i not in letters:
                letters[i] = 1
            else:
                letters[i] = letters[i] + 1

        for j in t:
            if j not in lettersTwo:
                lettersTwo[j] = 1
            else:
                lettersTwo[j] = lettersTwo[j] + 1
        
        for i in s:
            if i not in lettersTwo:
                return False
            else:
                if letters[i] != lettersTwo[i]:
                    return False
        
        return True
        