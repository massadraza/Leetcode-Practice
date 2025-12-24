class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        pointerA = 0
        pointerB = len(numbers) - 1

        while(pointerA < pointerB):
            temp = target - numbers[pointerA]
            if numbers[pointerB] < temp:
                pointerA = pointerA + 1
                pointerB = len(numbers) - 1
            elif numbers[pointerB] == temp:
                return [pointerA + 1, pointerB + 1]
            else:
                pointerB = pointerB - 1

        """   
        pointerA = 0
        pointerB = len(numbers) - 1

        while(pointerA < pointerB):
            currSum = numbers[pointerA] + numbers[pointerB]

            if currSum > target:
                pointerB = pointerB - 1
            elif currSum < target: 
                pointerA = pointerA + 1
            else:
                return [pointerA + 1, pointerB + 1]
