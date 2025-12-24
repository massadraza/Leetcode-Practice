class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        p = 0
        q = 1
        seen = set()
        
        if len(s) < 1:
            return 0

        seen.add(s[p])
        count = 1
        maxCount = 1

        while q < len(s):
            if s[q] not in seen:
                seen.add(s[q])
                count = count + 1
                maxCount = max(maxCount, count)
                q = q + 1
            else:
                p = p + 1
                seen.clear()
                if p < len(s):
                    seen.add(s[p])
                count = 1
                q = p + 1
        
        return maxCount
"""

