class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for index, num in enumerate(nums):
            if index > 0 and num == nums[index - 1]:
                continue 

            pointerA = index + 1
            pointerB = len(nums) - 1

            while(pointerA < pointerB):
                sum = nums[pointerA] + nums[pointerB] + num
                if sum < 0:
                    pointerA = pointerA + 1
                elif sum > 0: 
                    pointerB = pointerB - 1
                else:
                    result.append([num, nums[pointerA], nums[pointerB]])
                    pointerA = pointerA + 1
                    while nums[pointerA] == nums[pointerA - 1] and pointerA < pointerB:
                        pointerA = pointerA + 1

        return result
                

                    