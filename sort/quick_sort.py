# O(nlogn)
class Solution(object):
    def quick_sort(self, unsorted):
        length = len(unsorted)
        if length < 2:
            return unsorted
        # Use the last element as the first pivot
        pivot = unsorted.pop() # differ with 3_partition

        lesser, greater = [], []
        for i in unsorted:
            if i <= pivot:
                lesser.append(i)
            else:
                greater.append(i)
        return self.quick_sort(lesser) + [pivot] + self.quick_sort(greater)

s = Solution()
print(s.quick_sort([0,1,2,3,9,8]))
            