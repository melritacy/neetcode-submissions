class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(len(nums)):
            exclude=nums.pop(i)
            mul=1
            for j in range(0,len(nums)):
                mul=mul*nums[j]
            result.append(mul)
            nums.insert(i,exclude)
        return result
        