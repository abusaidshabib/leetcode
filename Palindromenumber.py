# https://leetcode.com/problems/palindrome-number/description/ (problem)

#shabib solution 1
# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         new_x = str(x)
#         reversed_x = str(x)[::-1]
#         return new_x == reversed_x

# shabib solution 2
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        temp = x
        reversed_x = 0
        while temp != 0:
            reversed_x = reversed_x * 10 + temp%10
            temp = temp // 10

        return x == reversed_x


x = 121
sol = Solution()
print(sol.isPalindrome(x))