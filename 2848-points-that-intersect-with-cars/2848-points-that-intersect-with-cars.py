class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        
        # sort the nums by first el
        nums.sort(key = lambda x:x[0])
        
        total_points = 0
        prev_end = -1
        
        for start , end in nums:
            if start > prev_end :
                total_points += end - start+1
            else:
                total_points += max(0,end-prev_end)
            prev_end = max(end,prev_end)
        return total_points