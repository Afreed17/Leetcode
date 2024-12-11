class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        
        elarray = []
        
        #sort the array based on first el
        nums.sort(key = lambda x:x[0])
        
        for i in range(len(nums)):
            start = nums[i][0]
            stop = nums[i][1]
            for j in range(start,stop+1):
                if j in elarray:
                    continue
                else:
                    elarray.append(j)
        return len(elarray)
        