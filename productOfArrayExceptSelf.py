class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
"""
        result = []
        for i in range(len(nums)):
            tempMult = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                tempMult = tempMult * nums[j]
            result.append(tempMult)

        return result
"""