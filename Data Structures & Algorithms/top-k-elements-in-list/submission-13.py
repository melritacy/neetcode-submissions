from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dict_nums=defaultdict(int)
        largest=[]

        # starting off with int
        for i in range(len(nums)):
            print(largest)
            dict_nums[nums[i]]+=1
            if (nums[i] not in largest):
                largest.append(nums[i])

        largest.sort(key=dict_nums.get,reverse=True)

        

        return largest [:k] 

        


        