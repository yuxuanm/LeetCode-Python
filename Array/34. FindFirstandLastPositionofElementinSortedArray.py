class Solution(object):
    def searchRange(self, nums, target):
        """
        binary search, search the left bound and right bound separately.
        runtime: 24ms beats 54.61%
        memory: 13.1mb beats 98.49%
        """
        return [self.findLeft(nums, target), self.findRight(nums, target)]

    def findLeft(self, nums, target):
        start = 0
        end = len(nums) - 1
        index = -1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                index = mid
                end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return index

    def findRight(self, nums, target):
        start = 0
        end = len(nums) - 1
        index = -1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                index = mid
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return index


if __name__ == "__main__":
    s = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(s.searchRange(nums, target))
