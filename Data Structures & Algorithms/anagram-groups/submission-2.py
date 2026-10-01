from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        
        groups = defaultdict(list)

        for i in strs:
            groups["".join(sorted(i))].append(i)

        return list(groups.values())
        """
        groups = defaultdict(list)
        for i in strs:
            letters = [0]*26
            for j in i:
                letters[ord(j) - ord('a')] +=1 
            groups[tuple(letters)].append(i)
        
        return list(groups.values())
            

        #letters[0] = a
        #lettrs[25] = z


        