class Solution(object):
    def fourSum(self, nums, target):
        """
        similar to question 15.3Sum
        firstly fix two numbers, and search the remaining two via binary search
        rank each individual combinations to control duplication
        """
        res = []
        nums = sorted(nums)
        for i in range(len(nums) - 3):
            for j in range(i+1, len(nums) - 2):
                remain = target - nums[i] - nums[j]
                start = j + 1
                end = len(nums) -1
                while start < end:
                    if nums[start] + nums[end] == remain:
                        tmp = sorted([nums[i], nums[j], nums[start], nums[end]])
                        if tmp not in res: # control duplications
                            res.append(tmp)
                        start = start + 1
                        end = end - 1
                    elif nums[start] + nums[end] > remain:
                        end = end - 1
                    else:
                        start = start + 1
        return res


if __name__ == "__main__":
    s = Solution()
    nums= [-1, 0, 1, 2, -1, -4]
    target = -1

    res = s.fourSum(nums, target)
    print(res)
