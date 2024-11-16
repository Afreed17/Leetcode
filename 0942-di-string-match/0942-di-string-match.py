class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        small = 0
        large = len(s)
        perm = []
        
        for i in s:
            if i == "I":
                perm.append(small)
                small += 1
            else:
                perm.append(large)
                large -= 1
        if s[-1] == "I":
            perm.append(small)
        else:
            perm.append(large)
        return perm
            
        