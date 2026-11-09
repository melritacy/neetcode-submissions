class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #preprocess
        string=[]
        for l in s:
            if (l.isalnum()):
                l = l.lower()
                string.append(l)
        pointer_1 = 0
        pointer_2 = len(string)-1
        while (pointer_1 < pointer_2):
            if(string[pointer_1]==string[pointer_2]):
                pointer_1+=1
                pointer_2-=1
            else:
                return False
        return True


            


