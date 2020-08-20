class Solution(object):
    def maxSubArray(self, nums):
        """
        dynamic programming
        iterate the array, for the current cell i, if nums[i-1] is negative, it has no contribution to the max sum, thus
        directly ignore the first i-1 items. Otherwise, add nums[i-1] + nums[i] for a new local maximum.
        runtime: 12 ms beats 99.83%
        """
        for i in range(1, len(nums)):
            nums[i] = nums[i] if nums[i - 1] < 0 else nums[i - 1] + nums[i]

        return max(nums)
        # res[1] = nums[1] if nums[0] + nums[1] < nums[1] else nums[0] + nums[1]
        # for i in range(2, len(nums)):
        #     if nums[i] < 0:
        #         res[i] = res[i - 1]
        #     else:
        #         res[i] = max(res[i - 1] + nums[i], nums[i])
        # max_sum = nums[0]
        # for i in res:
        #     if i > max_sum:
        #         max_sum = i
        # return max_sum


if __name__ == "__main__":
    s = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # nums = [1, 2, 3, 4, 5, 6]
    print(s.maxSubArray(nums))
