class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subMap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in subMap:
                return[subMap[diff],i]
            subMap[n] = i
        
        