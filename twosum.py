# shabib solution 1
# class Solution(object):
#     def twosum(self, nums, target):
#         for i in nums:
#             for j in nums:
#                 if i + j == target:
#                     return [nums.index(i), nums.index(j)]

# shabib solution 2
class Solution(object):
    def twosum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i




# nums = [2, 7, 11, 15]
nums = [4, 3, 90, -3]
target = 0
sol = Solution()
print(sol.twosum(nums, target))
