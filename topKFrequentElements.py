class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        visited = set()

        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            counter[nums[i]] = 1
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    counter[nums[j]] = counter[nums[j]] + 1
            visited.add(nums[i])

        visitedMap = set()
        result = []

        while(k != 0):
            max = 0
            num = None
            for x in nums:
                if counter[x] > max and x not in visitedMap:
                    max = counter[x]
                    num = x
            
            result.append(num)
            visitedMap.add(num)
            k = k - 1
            
        return result
                

