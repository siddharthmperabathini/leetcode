class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        cur_sum = nums[0]
        res = 123123
        while r < len(nums):
            if cur_sum >= target:
                res = min(res,(r-l+1))
                cur_sum -= nums[l]
                l += 1 
            else:
                r += 1
                if r == len(nums):
                    return 0 if res == 123123 else res
                cur_sum += nums[r]

        return 0 if res == 10000 else res



