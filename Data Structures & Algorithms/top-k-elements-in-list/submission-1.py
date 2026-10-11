class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        res = []
        for i in nums :
            d[i] = d.get(i, 0) + 1
        values=list(d.values())
        values.sort(reverse=True)
        value = values[k-1]
    
        for i in d :
            if d[i] >= value :
                res.append(i)
        return res[:k]