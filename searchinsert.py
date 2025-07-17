""" https://leetcode.com/problems/search-insert-position/submissions/1701507997/"""

class Solution(object):
    def searchInsert(self, nums, target):
        for i, v in enumerate(nums):
            if nums[-1] < target:
                return nums.index(nums[-1])+1
            elif v == target:
                return i
            elif v < target and v+1 == target:
                return i + 1
            elif v > target and v-1 == target:
                if i == 1:
                    return 1
                elif i == 0:
                    return 0
                else:
                    return i - 1 if i-1 >= 0 else 0
            if v > target:
                return 0





nums = [2,3,4,7,8,9]
target = 11
sol = Solution()
print(sol.searchInsert(nums, target))