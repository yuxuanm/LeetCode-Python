class Solution(object):
    def combinationSum2(self, candidates, target):
        '''
        backtrack, similar to problem 40.
        the only difference is use another index to indicate the position of the point that is currently been processed,
        all numbers before that index have already been checked thus we can directly ignore in the next iteration.
        runtime: 44 ms beats 59.35%
        memory: 12.7 mb beats 61.90%
        '''
        res = []
        tmpRes = []
        candidates.sort()

        def helper(candidates, target, tmpRes, preIndex):
            if target == 0 and tmpRes not in res:
                res.append(tmpRes[:])
                return
            for i in range(preIndex + 1, len(candidates)):  # start from the first number after the previous index
                if target - candidates[i] < 0:
                    break
                tmpRes.append(candidates[i])
                helper(candidates, target - candidates[i], tmpRes, i)
                tmpRes.pop()

        helper(candidates, target, tmpRes, -1)  # -1 indicates first round can start with candidates[0]
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [2, 5, 2, 1, 2]
    target = 5
    # nums = [10, 1, 2, 7, 6, 1, 5]
    # target = 8
    print(s.combinationSum2(nums, target))
