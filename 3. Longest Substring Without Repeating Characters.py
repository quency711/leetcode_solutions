class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        dic = {}
        max_value = start = 0 
             
        for idx, letter in enumerate(s):
            
            if letter in dic and start <=  dic[letter]:
                start = dic[letter] + 1 
                
            else:
                max_value = max(max_value, idx-start+1)
            
            dic[letter] = idx 
            
        return max_value
                                                                                                                                                                                        
        ##idea:sliding windows 
        ##思路:移动window,每走一步，先check此刻的letter是否已经和之前的重复了，如果重复了，那么起始点就会是这个letter在dic里面的index并且加上1（下一个点作为起始点避免和最新出现的值重复，比如a,b,c,b,e... 此时已经浏览到第四个值b，因为和之前的b重复了，那就要设置c做为起始值）
        ##并且要改变起点很重要的前提条件是此时的起点 比 此刻value之前出现的位置小，比如 t,m,m,z,u,t。
        # 1-看t,max=1,start=0;
        # 2-看m,max=2,start=0; 
        # 3-看m,start=2,max依然是2；
        # 4-看z,start仍然是2，max=2;
        # 5-看u，start=2， max=3
        # 6-看t, 假如不限制 前提条件，这时候改变了Start,变成了1，max=3 与我们想要的结果相违背了。所以这个时候要加前提条件就是 start <= 此刻value之前出现的位置
        
        
        ## 如果此刻浏览的值并没有出现在之前的值中，那么最大值有两种情况，要么就是之前就有出现过得最大值，或者就是在最新浏览到的值里找到了最大步长 
            
        
        