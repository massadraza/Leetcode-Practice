from typing import List

# Created by: Massad Raza
# 

class Solution: 

    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = dict()

        for i in nums:
            if i not in numbers:
                numbers[i] = 1
            else:
                return True
            
        return False
    
s = Solution()
result = s.hasDuplicate([5, 6, 7, 7])
print(result)
    