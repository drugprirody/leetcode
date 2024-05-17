class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        opened = 0
        closed = 0
        result = ""

        for c in s:
            if c == '(':
                opened +=1
                if opened > 1:
                    result +=c
            elif c == ')':
                closed +=1
                if closed < opened:
                    result +=c
                else:
                    closed = 0
                    opened = 0
        return result
    