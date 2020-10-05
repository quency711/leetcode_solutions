class Solution:
    def removeOuterParentheses(self, S: str) -> str:


      #Method 1 : 左括号就是+1, 右括号是-1， 当count=0时，就要做slice剥落，方法战胜97%
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        
        ct = left = 0
        res = ""

        for i in range(len(S)):
            
            if S[i] == "(":
                ct += 1
            elif S[i] == ")":
                ct -= 1

            if ct == 0 : 
                res += S[left+1:i]
                left = i +1 
        return res 