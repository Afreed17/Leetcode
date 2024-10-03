class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        newString = ''.join(filter(str.isalnum,s))
        return newString == newString[::-1]