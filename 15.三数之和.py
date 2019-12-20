#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums):
        nums.sort()
        result_list = list()
        for i in range(len(nums)-2):
            if i == 0 or nums[i] > nums[i-1]:
                left_node = i+1
                right_node = len(nums) - 1
                while left_node < right_node:
                    if nums[left_node] + nums[right_node] > -nums[i]:
                        right_node -= 1
                        # while nums[right_node] == nums[right_node+1] and left_node < right_node:
                        #     right_node -= 1
                    elif nums[left_node] + nums[right_node] < -nums[i]:
                        left_node += 1
                        # while left_node < right_node and nums[left_node] == nums[left_node-1]:
                        #     left_node += 1
                    else:                        
                        temp_list = [nums[i],nums[left_node],nums[right_node]]
                        result_list.append(temp_list)
                        left_node += 1
                        right_node -= 1
                        while left_node < right_node and nums[left_node] == nums[left_node-1]:
                            left_node += 1
                        while nums[right_node] == nums[right_node+1] and left_node < right_node:
                            right_node -= 1
                        
        return result_list
# @lc code=end

