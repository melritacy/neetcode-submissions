class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict={}
        t_dict={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] not in s_dict :
                s_dict[s[i]]=1
            else:
                s_dict[s[i]]+=1 
            if t[i] not in t_dict:
                t_dict[t[i]]=1
            else:
                 t_dict[t[i]]+=1

        for i in range(len(s)):
            if s[i] not in t_dict:
                return False
            elif s_dict[s[i]] != t_dict[s[i]]:
                return False
            
        return True
                



        