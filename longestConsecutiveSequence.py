class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        longest = 0

        for i in numSet: 
            if i - 1 not in numSet:
                counterIn = 0
                while (i + counterIn) in numSet:
                    counterIn = counterIn + 1
                longest = max(counterIn, longest)
        
        return longest