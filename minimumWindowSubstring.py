class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge Case
        if t == "":
            return ""
        
        # Initialize counts of T (need)
        countsT = {}
        for char in t:
            countsT[char] = 1 + countsT.get(char, 0)
        
        window = {}

        have = 0 
        need = len(countsT)

        result = [-1, -1]
        resultLength = float('infinity')

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countsT and window[c] == countsT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resultLength:
                    result = [l, r]
                    resultLength = (r - l + 1)
                window[s[l]] -= 1

                if s[l] in countsT and window[s[l]] < countsT[s[l]]:
                    have -= 1
                l += 1

        l = result[0]
        r = result[1]

        return s[l:r+1] if resultLength != float('infinity') else ""





        

