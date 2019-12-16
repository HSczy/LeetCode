#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for index, num in enumerate(nums):
            if map.get(target-num) is not None:
                return [map.get(target-num),index]
            map[num] = index
# @lc code=end