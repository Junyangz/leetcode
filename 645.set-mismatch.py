class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return [sum(nums) - sum(set(nums)), sum(range(1, len(nums)+1)) - sum(set(nums))]
#         stack = []
#         miss = len(nums)
#         nums = sorted(nums)
#         for i, n in enumerate(set(nums)):
#             if n != i + 1:
#                 miss = i + 1
#                 break
#         for i in nums:
#             if i not in stack:
#                 stack.append(i)
#             else:
#                 dup = i
#                 break
#         return [dup, miss]
                
        