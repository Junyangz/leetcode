# O(n2)
# 不稳定排序
class Solution(object):
    def selection_sort(self, unsorted):
        for i in range(len(unsorted) - 1):
            least = i 
            for k in range(i + 1,len(unsorted)):
                if unsorted[k] < unsorted[least]:
                    least = k
            unsorted[i], unsorted[least] = unsorted[least], unsorted[i]
        return unsorted

s = Solution()
print(s.selection_sort([9,8,7,6,5,4,3,2,1]))