class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        best = 0
        l = 0
        r = 0
        kk = 0
        while r < len(nums):
            if nums[r] == 0:
                kk += 1
            while kk > k:
                if nums[l] == 0:
                    kk -= 1
                l += 1
            best = max(best, r - l + 1)
            r += 1
        return best
                 
                
            