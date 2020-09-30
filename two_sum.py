class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        dic = {}
        #Better solution: run two loops at the same time 
        #思路：1.先过一遍所有数据，做好标号；2.第二次过哈希表的时候查下target-value是否在哈希表里，如果在，并且他的idx与value的idx不一样
        #就return结果
        for idx, value in enumerate(nums):
            dic[value] = idx
        
        for idx1, value in enumerate(nums):
            if target-value in dic:
                idx2 = dic[target - value]
                
                if idx1 != idx2:
                    return [idx1,idx2]
        
        #It has two for loop, will increase time complexity 
        # for idx, value in enumerate(nums):
        #     dic[value] = idx 
        #     for idx1, value in enumerate(nums):
        #         if target - value in dic: 
        #             idx2 = dic[target - value]
        #             if idx1 != idx2 :
        #                 return [idx1,idx2]

        