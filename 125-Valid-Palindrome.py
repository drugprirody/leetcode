class Solution:
    def isNotNeedSymbol(self,c):
        if ord(c.lower()) < 97 or ord(c.lower()) > 122:
                
            if (ord(c.lower()) < 48 or ord(c.lower()) > 57):
                return True
            
            return False

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
            
        while left < right:
            if self.isNotNeedSymbol(s[left]):
                left +=1
                continue 
            elif self.isNotNeedSymbol(s[right]):
                right -=1
                continue
            if s[left].lower() != s[right].lower():
                return False       
            left +=1
            right -=1
        return True