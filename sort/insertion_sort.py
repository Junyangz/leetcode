# 每一步将一个待排序的记录，插入到前面已经排好序的有序序列中去，直到插完所有元素为止
# O(n)~ O(n2)
class Solution(object):
    def insertion_sort(self, unsorted):
        for i in range(1, len(unsorted)):
            k = i 
            while k > 0 and unsorted[k - 1] > unsorted[k]:
                unsorted[k - 1], unsorted[k] = unsorted[k], unsorted[k - 1]
                k -= 1
        return unsorted

s = Solution()
print(s.insertion_sort([1,2,9,8,7,6,5,4,3,0]))

