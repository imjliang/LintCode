# 8 · Rotate Character Array

# 2022/11/14
# sol 1: 老题 
# 反转字符串三次
# 81ms Time Cost 6.07MB Memory Cost 98.60%


from typing import (
    List,
)

class Solution:
    """
    @param s: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotate_string(self, s: List[str], offset: int):
        # write your code here
        if not s: return s
        offset = offset % len(s)
        self.reverse(s, 0, len(s)-1)
        self.reverse(s, 0, offset-1)
        self.reverse(s, offset, len(s)-1)        
        
        return

    def reverse(self, s, l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return

  