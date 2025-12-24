class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        area = 0
        
        pointerA = 0
        pointerB = len(height) - 1

        while pointerA < pointerB:
            area = min(height[pointerA], height[pointerB]) * (pointerB - pointerA)
            
            if height[pointerA] < height[pointerB]:
                pointerA = pointerA + 1
            else:
                pointerB = pointerB - 1

            if area > maxArea:
                maxArea = area

        return maxArea


