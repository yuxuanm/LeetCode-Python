class Solution(object):
    def searchInsert(self, nums, target):
        """
        binary search, if there is a match, directly return the current index
        else, return the current index if nums[mid]> target, else return mid+1
        runtime: 16 ms beats 88.08%
        memory: 13mb beats 31.00%
        """
        mid = -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return mid if nums[mid] > target else mid + 1  # the index that insert into the array


if __name__ == "__main__":
    s = Solution()
    nums = [1, 3, 5, 6]
    target = 0
    print(s.searchInsert(nums, target))
