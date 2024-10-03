class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        result = strs[0]

        for i in range (1,len(strs)):
            string = strs[i]

            temp = ''

            for a , b in zip(result,string):
                if a == b :
                    temp += a
                else:
                    break
            result = temp
            if result == '':
                break
        return result