class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs :
            s = s + i + "@#@@"
        print(s)
        return s 
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            mot = ""
            while s[i:i+4] != "@#@@" and i + 4 < len(s) :
                mot+= s[i]
                i+=1
            strs.append(mot)
            i+=4
        return strs

