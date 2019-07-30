class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        answer = [0] * l
        answer[0] = 1
        
        for i in range(1, l):
            answer[i] = nums[i-1] * answer[i-1]
        
        R = 1
        for i in reversed(range(l)):
            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer
        
        
#         p = [0] * (len(nums)+1)
#         p[-1] = 1
#         res = 1
#         for i in range(len(nums)-1):
#             res *= nums[i]
#             p[i] = res

#         R = 1
#         for j in range(len(nums) - 1, -1, -1):
#             p[j] = p[j-1] * R
#             R *= nums[j]
            
#         return p[:-1]

        