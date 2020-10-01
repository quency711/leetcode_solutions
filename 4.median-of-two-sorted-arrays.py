class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        #sort array first, then find median 
        ##先sort 再找中间值
        
        nums1.extend(nums2)
        nums1.sort()
        
        length = len(nums1)
        
        if length % 2 == 0:
            return (nums1[int(length/2-1)] + nums1[int(length/2)])/2
        else:
            return nums1[int((length+1)/2-1)]
        
        