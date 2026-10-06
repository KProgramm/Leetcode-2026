class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for i in strs:
            result.append(str(len(i)) + "#" + i)

        return "".join(result)
    
    # 2#hi5#there
    def decode(self, s: str) -> List[str]:
        result = []
        index = 0
        while index < len(s):
            l = ""
            while s[index] != "#":
                l+= s[index]
                index +=1
            index +=1
            length = int(l)
            word = ""
            for i in s[index: index + length]:
                word += i
            result.append(word)
            index += length
        return result




