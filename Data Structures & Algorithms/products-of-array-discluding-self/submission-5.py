class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        solution = 1 # solution without the zero
        solution2 = 1 # if solution wounds uo being 0
        for i in range(len(nums)):
            if (nums[i]!=0):
                solution = solution *nums[i]
            solution2 = solution2 *nums[i]

        nums2=nums.copy()
        for i in range(len(nums)):
            print(nums)
            if(solution2==0 and nums[i]!=0):
                nums[i]=0
            elif(solution2==0 and nums[i]==0):
                nums[i] = solution # answer without the zero
                if(nums2.count(0)>1):
                    nums[i]=0
                elif(solution==1 and nums2.count(0)==1):
                    nums[i]=1*solution
                

            else:
                nums[i]= int(solution2/nums[i])

        return nums


        

        