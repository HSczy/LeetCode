#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        original_index = 0
        for i in range(1,len(nums)):
            if nums[i] == nums[original_index]:
                nums[i] = nums[-1]
            else:
                original_index = i
        nums.sort()
        for i in nums:
            if i == nums[-1]:
                return nums.index(i)+1
# @lc code=end

