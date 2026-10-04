class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range( len(nums) -1) :
            d = {}
            for j in range( i+ 1 ,len(nums)) :
                
                if nums[j] in d   :
                    s = tuple(sorted([nums[i], -(nums[i] + nums[j]) ,nums[j] ]))
                    res.add(s)
                d[-( nums[i] + nums[j] )]= j
      
        return [list(i) for i in res ]
        