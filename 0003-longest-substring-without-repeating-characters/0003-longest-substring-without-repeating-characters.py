class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) > 1:
            substrings = []
            for i in range (len(s)):
                temp = ''
                temp = temp + s[i]
                for j in range (i+1,len(s)):
                    if s[j] not in temp:
                        if j == len(s) - 1:
                            temp = temp + s[j]
                            substrings.append(temp)
                        temp = temp + s[j]
                    else:
                        substrings.append(temp)
                        break
            maxlen = 0 
            for el in substrings:
                if len(el) > maxlen:
                    maxlen = len(el)
            return maxlen
        elif len(s) == 1:
            return 1
        else:
            return 0
        