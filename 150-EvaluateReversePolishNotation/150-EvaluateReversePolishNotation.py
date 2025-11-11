# Last updated: 11/11/2025, 1:57:29 AM
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        mapping = {'+': operator.add, '/': lambda a,b: int(operator.truediv(a,b)), '-' : operator.sub, '*' : operator.mul}
        for char in tokens:
            if char in mapping:
                b = stack.pop()
                a = stack.pop()
                result = mapping[char](a,b)
                stack.append(result)
            else:
                stack.append(int(char))
    
        return stack[0]

        


        


        