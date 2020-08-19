class Solution(object):
    def combinationSum(self, candidates, target):
        """
        backtrack
        runtime: 36 ms beats 85.42%
        memory: 12.7 mb beats 80.21%
        """
        res = []
        tmpRes = []
        candidates.sort()
        self.subCombination(candidates, target, tmpRes, res, candidates[0] - 1)
        return res

    def subCombination(self, candidates, target, tmpRes, res, preNum):
        if target == 0:
            res.append(tmpRes[:])
            return

        for i in candidates:
            if target - i < 0:
                break
            if i < preNum:  # this indicate we have check this combination before, because the list is sorted, we only
                continue  # need to check numbers that no smaller than previous one
            tmpRes.append(i)
            self.subCombination(candidates, target - i, tmpRes, res, i)
            del tmpRes[len(tmpRes) - 1]


if __name__ == "__main__":
    s = Solution()
    nums = [2, 3, 5, 7]
    target = 8
    print(s.combinationSum(nums, target))
