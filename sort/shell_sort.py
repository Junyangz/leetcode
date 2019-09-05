class solution:
    # 不稳定排序，O(nlogn)
    def shell_sort(self, collection):
        # Marcin Ciura's gap sequence
        gaps = [701, 301, 132, 57, 23, 10, 4, 1]
        for gap in gaps:
            i = gap
            while i < len(collection):
                temp = collection[i]
                j = i
                while j >= gap and collection[j - gap] > temp:
                    collection[j] = collection[j - gap]
                    j -= gap
                collection[j] = temp
                i += 1

        return collection

s = solution()

print(s.shell_sort([1,2,3,4,5,6,9,8,7,0,-1,0]))