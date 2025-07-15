# https://leetcode.com/problems/roman-to-integer/description/

# class Solution(object):
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         roman = {
#             "I": 1,
#             "V":5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }
#         first_v = None
#         result = 0
#         for i in reversed(s):
#             if not first_v:
#                 first_v = i
#                 result = roman[i]
#             elif first_v and roman[first_v] < roman[i]:
#                 result += roman[i]
#             elif first_v and roman[first_v] > roman[i]:
#                 result -= roman[i]
#             elif roman[first_v] == roman[i]:
#                 result += roman[i]
#             print(result)
#
#             first_v = i
#
#         return result

class Solution(object):
    def romanToInt(self, s):
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        prev_value = 0

        for char in reversed(s):
            value = roman[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value

        return total



target = "DCCCXC"
sol = Solution()
print(sol.romanToInt(target))