class Solution(object):
    def search(self, nums, target):
        """
        Because the question requires time complexity of O(logn), the basic idea is binary search. As the array is
        rotated, thus the array has two circumstances.
        1st: mid value >= start value, means the left side of the array is strictly increasing.
        2nd: else, the second half is strictly increasing
        For each situation, the target can either be in the left half array or right half array
        Results: runtime : 28 ms
                 memory: 12.8 MB
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[start]: # 1st: left half array is strictly increasing
                if nums[start] <= target < nums[mid]: # target in the left half array
                    end = mid - 1
                else: # target in the right half array
                    start = mid + 1
            else: # 2nd: right half array is strictly increasing
                if nums[mid] < target <= nums[end]: # target in the right half array
                    start = mid + 1
                else: # target in the left half array
                    end = mid - 1
        return -1


if __name__ == "__main__":
    s = Solution()
    nums = [3, 1]
    target = 1
    print(s.search(nums, target))
