class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        two pointers, firstly fixed one number, another two pointers 'start','end' to indicate the other two
        numbers, if the three sum greater than target, then move 'end' to the left by one position.
        runtime: 56ms beats 91.75%
        memory: 12.8 mb beats 30.85%
        """
        nums=sorted(nums)
        minDiff = abs(nums[0] + nums[1] + nums[2] - target)
        minSum = nums[0] + nums[1] + nums[2]
        for i in range(0, len(nums) - 2):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                tmp_sum = nums[i] + nums[start] + nums[end]
                if tmp_sum > target: # sum is larger than target, then move end to left
                    if tmp_sum - target < minDiff:
                        minSum = nums[i] + nums[start] + nums[end]
                        minDiff = tmp_sum - target
                    end = end - 1
                elif tmp_sum < target: # sum is smaller than target, then move start to the right
                    if target - tmp_sum < minDiff:
                        minSum = nums[i] + nums[start] + nums[end]
                        minDiff = target - tmp_sum
                    start = start + 1
                else: # exactly match target, thus return target
                    return target
        return minSum


if __name__ == "__main__":
    s = Solution()
    nums = [-3,-2,-5,3,-4]
    target = -1

    res = s.threeSumClosest(nums, target)
    print(res)
