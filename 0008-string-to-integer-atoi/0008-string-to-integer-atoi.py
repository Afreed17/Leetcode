class Solution:
    def myAtoi(self, s: str) -> int:
    
        if not s:
            return 0
        
        res = ''
        s = s.strip()
        
        sign = 1
        index = 0
        n = len(s)
        
        if index < n and (s[index] == '+' or s[index] == '-'):
            sign = -1 if s[index] == '-' else 1 
            index += 1
            
        while index < n and s[index].isdigit():
            res += s[index]
            index += 1
            
        if not res:
            return 0
        
        out = sign * int(res)
        
        min_val = -2 ** 31 
        max_val = 2 ** 31 - 1
        
        if out < min_val :
            return min_val
        if out > max_val:
            return max_val
        return out
            
            
        