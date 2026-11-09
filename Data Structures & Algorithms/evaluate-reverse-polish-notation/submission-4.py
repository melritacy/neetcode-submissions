import operator 
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def truncate_div(a, b):
            return int(a / b)

        arm={"+":operator.add,"-":operator.sub,"*":operator.mul,"/":truncate_div}

        stack=[]
        result = 0
        for token in tokens:
            if token in arm.keys():
                print(stack)
                num_1 =stack.pop()
                num_2= stack.pop()
                result=arm[token](num_2,num_1)
                stack.append(result)
            else:
                stack.append(int(token))
        return(stack[0])



        

