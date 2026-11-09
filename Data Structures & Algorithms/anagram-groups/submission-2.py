from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        list_words=[]
        dict_ana = defaultdict(list)

        for i in strs:
            word = list(i)
            word.sort()
            word = str(word)
            if word not in dict_ana:
                dict_ana[word].append(i)
            else:
                dict_ana[word].append(i)

        for listy in dict_ana.values():        
            list_words.append(listy)
            
        return list_words

            

        
        