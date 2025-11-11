# Last updated: 11/11/2025, 1:57:49 AM
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for portion in path.split('/'):
            if portion == "..":
                if stack:
                    stack.pop()
            elif portion == '.' or not portion:
                continue #continue not break
            else:
                stack.append(portion)
        print(stack)
        string = "/" + "/".join(stack)
        return (string)
        

        
        

        