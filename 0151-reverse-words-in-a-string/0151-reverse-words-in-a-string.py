class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split(" ")
        s = s[::-1]
        new = "" 
        for el in s :
            if el == "":
                continue
            new = new + el + " "
        return new.strip()