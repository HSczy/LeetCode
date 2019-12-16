#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_result = 0
        no_repeat_list = []
        for i in s:
            if i in no_repeat_list:
                no_repeat_list = no_repeat_list[no_repeat_list.index(i) + 1:]
            no_repeat_list.append(i)
            if max_result < len(no_repeat_list):
                max_result = len(no_repeat_list)
        return max_result 
# @lc code=end

