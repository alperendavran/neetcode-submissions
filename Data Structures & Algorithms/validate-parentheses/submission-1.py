from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map = {
            "[": "]",
            "(": ")",
            "{": "}"
        }

        stack = deque() # LIFO must be implemented

        for each in s:

            if each in brackets_map.keys():
                stack.append(each)
            else:
                if not stack:
                    return False

                if brackets_map[stack.pop()] != each:
                    return False
        
        return not stack 