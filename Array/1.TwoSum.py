class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i]+nums[j]==target:
                    res.append(i)
                    res.append(j)
                    return res
        return res

if __name__=='__main__':
    nums = [2,7,11,15]
    target = 9

    s=Solution()
    res = s.twoSum(nums,target)
    print(res)