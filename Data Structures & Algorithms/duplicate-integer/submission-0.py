class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        letterdict={}
        for i in range(len(nums)):
            if nums[i] not in letterdict:
                letterdict[nums[i]] = 1
            else:
                return True
        return False            
        