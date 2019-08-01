#!/usr/bin/env python
#-*-coding:utf-8-*-
# 最好、最坏和平均时间复杂度均为O(nlogn)，空间复杂度为O(1), 不稳定排序
# 堆是具有以下性质的完全二叉树：每个结点的值都大于或等于其左右孩子结点的值，称为大顶堆；或者每个结点的值都小于或等于其左右孩子结点的值，称为小顶堆
# 堆排建立最大堆时是从最后一个非叶子节点开始从下往上调整的
# 大顶堆：arr[i] >= arr[2i+1] && arr[i] >= arr[2i+2]  
# 小顶堆：arr[i] <= arr[2i+1] && arr[i] <= arr[2i+2] 
def heap_sort(lst):
    def sift_down(start, end):
        """最大堆调整"""
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and lst[child] < lst[child + 1]:
                child += 1
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break

# 创建最大堆
    # 从最后一个非叶子节点开始调整 n / 2 - 1 
    for start in range((len(lst) - 2) // 2, -1, -1):
        sift_down(start, len(lst) - 1)

# 堆排序
    for end in range(len(lst) - 1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        sift_down(0, end - 1)
    return lst


def main():
    l = [9, 2, 1, 7, 6, 8, 5, 3, 4]
    heap_sort(l)


if __name__ == "__main__":
    main()