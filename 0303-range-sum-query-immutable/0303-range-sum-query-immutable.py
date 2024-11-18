class NumArray:

    def __init__(self, nums: List[int]):
        self.TheList = nums
        

    def sumRange(self, left: int, right: int) -> int:
        Sum = 0
        for i in range(left,right+1):
            Sum = Sum + self.TheList[i]
        return Sum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)