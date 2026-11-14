class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i , x in enumerate(strs) :
            count =[0]*26
            for c in x :
                count[ord(c)-ord('a')]+=1
            d[tuple(count)].append(x)
        
        return list(d.values() )
    
            
            