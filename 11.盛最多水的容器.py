#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height):
        left_node,right_node,max_area = 0,len(height) - 1,0
        while left_node != right_node:
            if height[left_node] < height[right_node]:
                max_area,left_node = max(max_area,(right_node-left_node)*height[left_node]),left_node + 1
            else:
                max_area,right_node = max(max_area,(right_node-left_node)*height[right_node]),right_node - 1
        return max_area       
# @lc code=end

