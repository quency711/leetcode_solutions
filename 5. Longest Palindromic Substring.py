class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        ##idea : extend function 
        
        n = len(s)
        if n ==0:
            return ""
        res = s[0]  ##return result 
        
        #extend函数
        #什么情况下做extend? 当i在string之间，并且他们所处的位置string是一样的
        #怎么做extend呢？把idx往两边移动一下
        def extend(i,j,s):
            while (i>=0 and j<=n-1 and s[i] == s[j]): 
                i = i-1
                j = j+1
            return s[i+1:j] 
        
        #对于每一个字母都做extend，有两种情况，例子，字母a往两边做extend;或者aba往两边做extend看具体哪个return出来的结果更好
        for i in range(n-1):
            e1 = extend(i,i,s)
            e2 = extend(i,i+1,s)
            
            if max(len(e1),len(e2)) > len(res):
                res = e1 if len(e1) > len(e2) else e2 
            
        return res
                
                
            
            
            