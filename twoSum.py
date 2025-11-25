# Created by: Massad Raza

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        visited = {}

        for index, val in enumerate(nums):
            if target - val in visited:
                return [visited[target - val], index]
            visited[val] = index
        

                
        
        