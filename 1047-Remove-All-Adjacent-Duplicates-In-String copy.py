class Solution:
    def removeDuplicates(self, s: str) -> str:
        i = 1
        while True:
            if s[i] == s[i-1]:
                s = s[:i-1]+ s[i+1:]
                i -= 2
            i += 1
            if len(s)-1 < i or len(s)-1 < 1:
                break
            if i == 0:
                i+=1
        return s