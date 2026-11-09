class Solution:
    def isValid(self, s: str) -> bool:
        open_bracket={'(':')','[':']','{':'}'}

        stack =[]
        for i in range(len(s)):
            print(s[i])
            if s[i] in open_bracket.keys() :
                stack.append(s[i])
            elif s[i] in open_bracket.values():
                if not stack:
                    return False
                bracket = stack.pop()
                if open_bracket[bracket]!=s[i]:
                    return False

        
        return len(stack)==0
                

        