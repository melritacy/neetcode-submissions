from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = defaultdict(int)
        
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in dict_nums:
                return [dict_nums[difference],i]
            else :
                dict_nums[nums[i]]=i

        
            