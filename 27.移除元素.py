#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        original_index = 0
        while original_index <= len(nums) - 1:
            if nums[original_index] == val:
                nums.remove(val)
                original_index -= 1
            original_index += 1
        return len(nums)
# @lc code=end

