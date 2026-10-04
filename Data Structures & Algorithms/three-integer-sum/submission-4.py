class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range( len(nums)) :
            d = {}
            for j in range( len(nums)) :
                
                if i!=j and  nums[j] in d  and nums.index(-(nums[j] + nums[i])) != i :
                    s = [nums[i], -(nums[i] + nums[j]) ,nums[j] ]
                    s.sort()
                    if s not in res : res.append(s)
                d[-( nums[i] + nums[j] )]= nums[j]
        return res


        