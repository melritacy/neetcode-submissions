from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dict_num = defaultdict(int)
        for i in nums:
            if i not in dict_num:
                dict_num[i]=1
            else:
                return True
        return False
        