class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smList = []
        gtList = []
        eqList = []
        
        
        for el in nums:
            if el > pivot:
                gtList.append(el)
            elif el < pivot:
                smList.append(el)
            else:
                eqList.append(el)
                
        return smList + eqList + gtList
                
                
    