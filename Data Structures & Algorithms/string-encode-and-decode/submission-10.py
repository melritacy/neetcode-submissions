class Solution:

    def encode(self, strs: List[str]) -> str:
        string=""
        for word in strs:
            string+=str(len(word))
            string+="#"
            string+=word
        print(string)
        return string

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        result=[]
        while i <len(s):
            print(i)
            if(s[i])=="#":
                num = int(s[j:i])
                print(num,"num")
                result.append(s[i+1:i+1+num])
                print(result,"result")
                i=i+num+1
                j=i
            else:
                i+=1            
        return result


            

