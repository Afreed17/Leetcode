class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stringCount = {}
        
        if len(s) != len(t):
            return False
        
        for char in s:
            if char in stringCount :
                stringCount[char] += 1
            else:
                stringCount[char] = 1
                
        for char in t:
            if char in stringCount :
                stringCount[char] -= 1
                if stringCount[char] < 0:
                    return False
            else:
                return False
        
        for value in stringCount.values():
            if value != 0:
                return False
        return True