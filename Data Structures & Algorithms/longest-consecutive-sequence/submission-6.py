
from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums.sort()
        count = 1
        largest = 1

        if(len(nums)==0):
            return 0
        for i in range(len(nums)-1):
            if (nums[i]+1==(nums[i+1])):
                count+=1
                if (count>largest):
                    largest = count
            elif (nums[i]==(nums[i+1])):
                continue
            else:
                count=1
        return largest






            
        