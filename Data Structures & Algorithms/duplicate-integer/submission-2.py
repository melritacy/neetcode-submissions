from collections import defaultdict 

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        numbers = defaultdict(int)

        for i in nums:
            if i in numbers.keys():
                return True
            else:
                numbers[i] = 1

        return False



        