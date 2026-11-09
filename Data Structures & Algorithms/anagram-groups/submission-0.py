class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list=defaultdict(list)
        output=[]
        for s in strs:
            sorted_str=tuple(sorted(s))
            anagram_list[sorted_str].append(s)

        for values in anagram_list.values():
            output.append(values)
        return output


        


                    

        