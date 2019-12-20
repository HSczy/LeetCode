class Solution:
    def removeElement(self, nums, val):
        original_index = 0
        while original_index < len(nums) - 1:
            if nums[original_index] == val:
                nums.remove(val)
                original_index -= 1
            original_index += 1
        return len(nums)
if __name__ == "__main__":
    print(Solution().fourSum([-1,0,-5,-2,-2,-4,0,1,-2],-9))