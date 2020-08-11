class Solution(object):
    # Method 1: optimize method 2
    def removeElement(self, nums, val):
        """
        idea from LeetCode
        runtime: 20 ms beats 70.8%
        memory: 12.7 mb beats 62.08%
        """
        i = 0
        for j in range(0, len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i = i + 1
        return i


# Method 2
# def removeElement(self, nums, val):
#     """
#     similar to question 26, use two pointers
#     the first pointer indicates the current max effective length
#     the second pointer scan through the whole array
#     runtime: 20ms beats 70.8%
#     memory: 12.8 mb beats 18.65%
#     """
#     i = 0
#     j = 0
#     while j < len(nums):
#         while j < len(nums) and nums[j] != val:
#             nums[i] = nums[j]
#             i = i + 1
#             j = j + 1
#         while j < len(nums) and nums[j] == val:
#             j = j + 1
#         if j >= len(nums):
#             return i
#         nums[i] = nums[j]
#         i = i + 1
#         j = j + 1
#     return i


if __name__ == "__main__":
    s = Solution()
    nums = [3, 2, 2, 3]
    print(s.removeElement(nums, 2))
