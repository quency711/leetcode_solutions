class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # nums[:] = list(sorted(set(nums)))
        # return len(nums)

        #双指针思想

        left = 0 
        right = 1 

        while right < len(nums) :
            if nums[left] == nums[right]:
                right += 1 
            else:
                nums[left+1] = nums[right]
                left += 1
                right +=1 

        return left+1 
        
