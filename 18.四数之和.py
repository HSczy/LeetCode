#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums, target):
        nums.sort()

        result_list = []
        for first_num_index in range(len(nums)-3):
            if first_num_index == 0 or nums[first_num_index] > nums[first_num_index-1]:
                temp_list = nums[first_num_index+1:]
                for second_num_index in range(len(temp_list)-2):
                    if second_num_index == 0 or temp_list[second_num_index] > temp_list[second_num_index-1]:
                        left_node = second_num_index + 1
                        right_node = len(temp_list) - 1
                        while left_node < right_node:
                            if temp_list[left_node] + temp_list[right_node] > target-(temp_list[second_num_index] + nums[first_num_index]):
                                right_node -= 1
                            elif temp_list[left_node] + temp_list[right_node] < target-(temp_list[second_num_index] + nums[first_num_index]):
                                left_node += 1
                            else:
                                result_list.append([nums[first_num_index],temp_list[second_num_index],temp_list[left_node],temp_list[right_node]])
                                left_node += 1;right_node -= 1
                                while left_node < right_node and temp_list[left_node] == temp_list[left_node-1]:
                                    left_node += 1
                                while left_node < right_node and temp_list[right_node] == temp_list[right_node+1]:
                                    right_node -= 1
        return result_list

    def get_num_sum(self, nums_list,target,count_num):
        if count_num >2:
            target = target-nums_list[0]
            nums_list = nums_list[1:]
            count_num = count_num - 1
            self.get_num_sum(nums_list,target,count_num)
        else:
            temp_list = list()
            left_node = 0
            right_node = len(nums_list) - 1
            while left_node < right_node:
                if nums_list[left_node] + nums_list[right_node]< target:
                    left_node += 1
                elif nums_list[left_node] + nums_list[right_node] < target:
                    right_node -= 1
                else:
                    temp_list.append([nums_list[left_node],nums_list[right_node]])
                    left_node += 1;right_node -= 1
                    while left_node < right_node and nums_list[left_node] == nums_list[left_node -1]:
                        left_node += 1
                    while left_node < right_node and nums_list[right_node] == nums_list[right_node + 1]:
                        right_node -= 1
            return 



# @lc code=end

