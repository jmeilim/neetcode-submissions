class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i , x in enumerate(strs) :
            if tuple(sorted(x)) not in d :
                d[tuple(sorted(x))] = [x]
            else :
                d[tuple(sorted(x))].append(x)
        res = [ i for i in d.values()]
        return res 

            
            