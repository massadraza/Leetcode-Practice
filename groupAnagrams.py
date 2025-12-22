class Solution:

    # Created by Massad Raza 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Inefficient Solution (uses sorting)
        # using a defaultdict() automatically assigns a key of whatever you suggested
        strs2 = defaultdict(list)

        # Using sorted(S) returns a list of each individual character
        # Must join using join() function with the character associated
        """
       
        for s in strs:
            stringSorted = ''.join(sorted(s))
            strs2[stringSorted].append(s)
        return list(strs2.values()) 
        
        """

        # Efficient Solution
         