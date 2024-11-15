class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        
        breakP = len(nums) - 1
        while nums[breakP] <= nums[breakP-1] and breakP > 0 :
            breakP -= 1
        
        if breakP == 0:
            nums.reverse()
        else:
            swap1 = breakP - 1

            break2 = len(nums) - 1
            while nums[swap1] >= nums[break2]:
                break2 -= 1
            swap2 = break2

            nums[swap1],nums[swap2] = nums[swap2],nums[swap1]
            
            l , r = breakP , len(nums) - 1
            while l < r :
                nums[l] , nums[r] = nums[r] , nums[l]
                l += 1
                r -= 1
        
            
        
                