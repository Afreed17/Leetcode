class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        stringMap = {}
        if len(s) == len(t):
            for i in range (len(s)):
                if s[i] in stringMap:
                    if stringMap[s[i]] != t[i]:
                        return False
                else:
                    if t[i] in stringMap.values():
                        return False
                    stringMap[s[i]] = t[i]
        return True
        