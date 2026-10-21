from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = defaultdict(list)


        for i in strs: #loops over each of the strings in the list 
            occurances = [0] * 26

            for j in i:
                occurances[ord(j) - ord('a')] += 1
            
            seen[tuple(occurances)].append(i)
        
        return list(seen.values())

