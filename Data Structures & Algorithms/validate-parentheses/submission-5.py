class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMap = {")": "(", "}": "{", "]": "["} 

        for b in s: 
            if b in bracketMap: 
                if stack and stack[-1] == bracketMap[b]: 
                    stack.pop() 
                else:
                    return False 
            else: 
                stack.append(b) 
        
        return True if not stack else False

            