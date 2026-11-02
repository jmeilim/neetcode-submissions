class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len( nums )

        if n == 1 : return nums[0]
        if n == 2 : return min( nums[1], nums[0] )
        min1 = self.findMin( nums[n//2:] )
        min2 = self.findMin( nums[:n//2] )
        return min( min1 , min2)