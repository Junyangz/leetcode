import pysnooper

# 稳定排序，需O(n)额外空间，时间复杂度O(nlogn)
class solution:

    @pysnooper.snoop()
    def merge_sort(self, collection):

        def merge(left, right):
            result = []

            while left and right:
                result.append((left if left[0] <= right[0] else right).pop(0))
            
            return result + left + right
        
        if len(collection) <= 1:
            return collection
        
        mid = len(collection) // 2

        return merge(self.merge_sort(collection[:mid]), self.merge_sort(collection[mid:]))

s=solution()

print(s.merge_sort([1,2,3,4,5,6,9,8,7,0,-1,0]))