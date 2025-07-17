# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/ (problem)

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        previous = nums[0]
        index = 1
        for i,v in enumerate(nums):
            if previous != v:
                nums[index] = v
                index += 1
            previous = v

        return index

nums = [1,1,2]
sol = Solution()
print(sol.removeDuplicates(nums))