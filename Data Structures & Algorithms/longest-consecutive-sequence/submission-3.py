class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if(len(nums)>0):
            sorted_array=sorted(nums)
            pointer = sorted_array[0]
            count = 1
            order_num=[1]
        else:
            return 0

        # starting the list
        for i in range(1,(len(sorted_array))):
            if (sorted_array[i] == pointer+1):
                count+=1
                order_num.append(count)
            elif (pointer+ 1<sorted_array[i]):
                count = 1
                order_num.append(count)
            pointer = sorted_array[i]
        return max(order_num)
            
        