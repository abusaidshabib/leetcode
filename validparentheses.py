


# https://leetcode.com/problems/valid-parentheses/ (problem)

class Solution(object):
    def isValid(self, s):
        paren = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        result = []
        if len(s) == 0:
            return False
        elif len(s) % 2 != 0:
            return False
        for i in s:
            if i not in paren:
                result.append(i)
            elif len(result) > 0 and result[-1] == paren[i]:
                result.pop()
            else:
                return False
        return len(result) == 0



s = "]{"
sol = Solution()
print(sol.isValid(s))