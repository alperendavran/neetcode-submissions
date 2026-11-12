from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map = {
            "[": "]",
            "(": ")",
            "{": "}"
        }

        stack = deque()

        for char in s:
            if char in brackets_map:
                # Açılış parantezini hatırla
                stack.append(char)

            else:
                # Eşleşebileceği açılış yok
                if not stack:
                    return False

                opening = stack.pop()

                # Son açılışın kapanışı bu karakter mi?
                if brackets_map[opening] != char:
                    return False

        # Kapanmamış açılış kalmamalı
        return not stack