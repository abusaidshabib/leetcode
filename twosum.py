# shabib solution 1
class Solution(object):
    def twoSum(self, nums, target):
        for i in nums:
            for j in nums:
                if i + j == target:
                    return [nums.index(i), nums.index(j)]



nums = [2, 7, 11, 15]
target = 9
sol = Solution()
print(sol.twoSum(nums, target))
