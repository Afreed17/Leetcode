class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = {}
        for i in nums :
            if i in colors:
                colors[i] += 1
            else:
                colors[i] = 1
                
        for i in range(len(nums)):
            if 0 in colors and colors[0] > 0:
                nums[i] = 0
                colors[0] -= 1
            elif 1 in colors and colors[1] > 0 :
                nums[i] = 1
                colors[1] -= 1
            else:
                nums[i] = 2
                colors[2] -= 1