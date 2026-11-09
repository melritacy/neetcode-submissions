from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = set(s) 
        m = defaultdict(str, {i:0 for i in s})
       
        n = set(t)
        n = defaultdict(str, {j:0 for j in t})

        for i in s:
            m[i]+=1

        for j in t:
            n[j]+=1

        return m==n


        