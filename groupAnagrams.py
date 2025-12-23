class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        words = []
        result = []

        for i in range(len(strs)):
            sortedWord = ''.join(sorted(strs[i]))
            words.append(sortedWord)

        visited = set()

        for index in range(len(words)):
            if index in visited:
                continue 

            currWordSorted = words[index]
            temp = []
            temp.append(strs[index])
            visited.add(index)

            for i in range(index + 1, len(words)):
                if currWordSorted == words[i] and i not in visited:
                    temp.append(strs[i])
                    visited.add(i)
            result.append(temp)

        return result    
        """            