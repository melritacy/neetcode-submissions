from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_list = list(s)
        # since happening in place, don't need to reassign to new variable
        s_list.sort()

        t_list = list(t)
        t_list.sort()

        if(s_list == t_list):
            return True
        else:
            return False




        