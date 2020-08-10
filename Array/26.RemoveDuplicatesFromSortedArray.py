class Solution(object):
    def removeDuplicates(self, nums):
        """
        two pointers, the first pointer point to the effective first n numbers
        the second pointer scan through the whole array
        only use two extra space
        runtime: 36 ms beats 48.19%
        memory: 13.9 mb beats 86.36%
        """
        i = 0
        j = 1
        while j < len(nums):
            if nums[j] == nums[j - 1]: # duplicate values
                j = j + 1
                continue
            i = i + 1
            nums[i] = nums[j]
            j = j + 1
        return i + 1


if __name__ == "__main__":
    s = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(s.removeDuplicates(nums))
