'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = 0
        x_copy = x
        while x:
            temp = x%10
            x = x//10
            s = s*10 +temp

        return s == x_copy

s = Solution()
x = 10
print(s.isPalindrome(x))

