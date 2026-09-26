class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums) -1 
        if r == -1 : return -1
        if r == 0 : return 0 if target == nums[0] else -1
        while l <= r :
            m = (l+r)//2
            print(m)
            if nums[m] < target :
                l = m +1
                
            else :
                r = m - 1
        return l if ( l< len(nums) and nums[l]==target) else -1