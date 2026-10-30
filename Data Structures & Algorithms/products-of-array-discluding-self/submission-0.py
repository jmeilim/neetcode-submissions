class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p  = 1 
        null = 0
        for x in nums :
            if x != 0 :
                p *= x 
            else : 
                null += 1
        res = [0]*len(nums)
        if null > 1 : return res
        res = [0]*len(nums)
        for i in range ( len(nums)) :
            if nums[i]==0 :
                res = [0]*len(nums)
                res[i] = p
                return res
            else :
                res[i] = int(p/nums[i])



        return res