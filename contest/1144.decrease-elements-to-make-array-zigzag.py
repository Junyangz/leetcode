class Solution:
    def movesToMakeZigzag(self, A: List[int]) -> int:
        A = [math.inf] + A + [math.inf]
        res = [0, 0]
        for i in range(1, len(A) - 1):
            res[i % 2] += max(0, A[i] - min(A[i-1], A[i+1]) + 1)
        return min(res)
        
        #dp = [0] * (len(nums) + 1)
        # res_e = 0
        # res_o = 0
        # for i in range(len(nums) - 1):
        #     if i % 2 == 0:
        #         if i == 0 and nums[i] <= nums[i+1]:
        #             res_e += nums[i+1] - nums[i] + 1
        #         if i >= 2 and nums[i] <= nums[i-1]:
        #             res_e += nums[i-1] - nums[i] + 1
        #         elif i >= 2 and max(nums[i-1] + 1, nums[i]) <= nums[i+1]:
        #             res_e += nums[i+1] - max(nums[i-1] + 1, nums[i]) + 1
        #     if i % 2 == 1:
        #         if i >= 1 and nums[i] <= nums[i-1]:
        #             res_o += nums[i-1] - nums[i] + 1
        #         elif max(nums[i-1] + 1, nums[i]) <= nums[i+1]:
        #             res_o += nums[i+1] - max(nums[i-1] + 1, nums[i]) + 1
        # if len(nums) % 2 == 1:
        #     if nums[-1] <= nums[-2]:
        #         res_e += nums[-2] - nums[-1] + 1
        # if len(nums) % 2 == 0:
        #     if nums[-1] <= nums[-2]:
        #         res_o += nums[-2] - nums[-1] + 1
        # return min(res_e, res_o)