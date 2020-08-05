class Solution(object):
    # def twoSum(self, nums, target):
    #     '''
    #     Brute force
    #     runtime: 3560 ms
    #     memory: 13.5 mb
    #     '''
    #     for i in range(len(nums)):
    #         for j in range(i+1,len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return i,j

    # def twoSum(self, nums, target):
    #     """
    #     one iteration
    #     runtime: 984 ms beats 39.57%
    #     memory: 13.4 mb beats 93.51%
    #     """
    #     for i in range(len(nums)):
    #         if target - nums[i] in nums:
    #             index = nums.index(target-nums[i])
    #             if i == index:
    #                 continue
    #             else:
    #                 return i,index

    def twoSum(self, nums, target):
        """
        use a dictionary, largely reduce runtime
        runtime: 36 ms beats 92.36%
        memory: 14.1 mb beats 19.06%
        """
        d={}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return i,d[target- nums[i]]
            else:
                d[nums[i]]=i


if __name__ == '__main__':
    # nums = [3, 3]
    nums = [3,2,4]
    target = 6

    s = Solution()
    res = s.twoSum(nums, target)
    print(res)
