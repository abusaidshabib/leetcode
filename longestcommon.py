# https://leetcode.com/problems/longest-common-prefix/description/ (problem)
# shabib solution 1
# class Solution(object):
#     def longestCommonPrefix(self, strs):
#
#         if len(strs) == 1:
#             return strs[0]
#         elif len(strs) == 0:
#             return ""
#
#
#         one_str = sorted(strs, key=len, reverse=True).pop()
#         result = ""
#         for i,v in enumerate(one_str):
#             array_len = 0
#             for j,w in enumerate(strs):
#                 array_len += 1
#                 if w and w[i] != v:
#                     return result
#                 elif array_len == len(strs) and w and w[i] == v:
#                     result += v
#
#
#         return result

# llm solution
class Solution(object):
    def longestCommonPrefix(self, strs):
        # Handle edge cases
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        # Find the shortest string length to limit comparisons
        min_len = min(len(s) for s in strs)
        result = ""

        # Compare characters at each position
        for i in range(min_len):
            char = strs[0][i]  # Take character from first string
            # Check if this character matches in all strings
            for s in strs[1:]:
                if s[i] != char:
                    return result
            result += char

        return result


lstrs = ["aaa","aa","aaa"]
sol = Solution()
print(sol.longestCommonPrefix(lstrs))