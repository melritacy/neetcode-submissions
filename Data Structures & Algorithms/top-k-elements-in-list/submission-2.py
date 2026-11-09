class Solution:
    from collections import defaultdict
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        integer_list=defaultdict(int)
        result=[]
    
        for integer in nums:
            integer_list[str(integer)]+=1
        
        sorted_values=sorted(integer_list.items(),key = lambda x:x[1],reverse=True)
        print(sorted_values)
        total_index=(len(sorted_values))
        for values in range(0,k):
            result.append((sorted_values[values][0]))
        print((result))

        return result