class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums

        j = 1
        while nums[j] <= nums[j - 1]:  # check if the array is already in desc order
            if j == len(nums) - 1:
                return self.sort(nums)
            j = j + 1

        j = len(nums) - 1
        for j in range(len(nums) - 1, 0, -1):
            if nums[j] < nums[j - 1]:
                continue
            return self.swapandsort(nums, j - 1)

    def swapandsort(self, nums, index):
        """
        when call this function, there is some point that nums[index] < nums[index+1]
        """
        minDiff = nums[index + 1] - nums[index]
        i = index + 1
        j = i
        while i < len(nums):
            if 0 < nums[i] - nums[index] < minDiff:
                minDiff = nums[i] - nums[index]
                j = i
            i = i + 1
        tmp = nums[index]
        nums[index] = nums[j]
        nums[j] = tmp
        return nums[0:index + 1] + sorted(nums[index + 1:len(nums)])

    def sort(self, nums):
        """
        in this situation, the array is already in desc order, thus reverse array
        """
        start = 0
        end = len(nums) - 1
        while start < end:
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
            start = start + 1
            end = end - 1
        return nums


if __name__ == "__main__":
    s = Solution()
    nums = [1, 3, 2]
    print(s.nextPermutation(nums))
