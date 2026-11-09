class Solution:

    encoding=[]
    decoding=[]

    def encode(self, strs: List[str]) -> str:
        if (len(strs)==0):
            return "nullify"
        if (strs==[""]):
            return ""
        sentence = "//:://".join(strs)
        return sentence
            

    def decode(self, s: str) -> List[str]:
        if (s=="nullify"):
            return []
        decoding = s.split("//:://")
        return decoding
        

