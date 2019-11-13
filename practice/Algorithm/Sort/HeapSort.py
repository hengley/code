# -*- coding: utf-8 -*-
# @Time    : 2018/3/14 16:00
# @File    : HeapSort.py
# detail

from Algorithm.Sort.generateArrayHelper import generateArray
import random

'''
利用堆（heaps）这种数据结构来构造的一种排序算法。
堆是一个近似完全二叉树结构，并同时满足堆属性：即子节点的键值或索引总是小于（或者大于）它的父节点。

堆排序步骤：

1.将数据构建成堆，这里的堆指完全二叉树（不一定是满二叉树）

2.将堆调整为最小堆或最大堆

3.此时堆顶已经为最大数或最小数，可以对下面的分支堆再进行调堆即可，此处采用的是将堆顶数取出，再调堆
'''
# def ajust_heap(heap, root, heapsize):
#     lchild = 2*root + 1
#     rchild = 2*root + 2
#     max = root
#     while lchild < heapsize and heap[lchild] > heap[max]:
#         max = lchild
#     while rchild < heapsize and heap[rchild] > heap[max]:
#         max = rchild
#     if max != root:
#         heap[max], heap[root] = heap[root], heap[max]
#         ajust_heap(heap, max, heapsize)
#
# def build_max_heap(heap):
#     heapsize = len(heap)
#     for i in xrange((heapsize - 2)//2, -1, -1):
#         ajust_heap(heap, i, heapsize)
#
# def heap_sort(heap):
#     build_max_heap(heap)
#     for i in range(len(heap) - 1, -1 , -1):
#         heap[0], heap[i] = heap[i], heap[0]
#         ajust_heap(heap, 0, i)
#     return heap
#

# new_lists = heap_sort(generateArray(10))
# print (new_lists)


def MAX_Heapify(heap, HeapSize, root):  # 在堆中做结构调整使得父节点的值大于子节点

    left = 2*root + 1
    right = left + 1
    larger = root
    if left < HeapSize and heap[larger] < heap[left]:
        larger = left
    if right < HeapSize and heap[larger] < heap[right]:
        larger = right
    if larger != root:   # 如果做了堆调整则larger的值等于左节点或者右节点的，这个时候做对调值操作
        heap[larger], heap[root] = heap[root],heap[larger]
        MAX_Heapify(heap, HeapSize, larger)


def Build_MAX_Heap(heap):  # 构造一个堆，将堆中所有数据重新排序
    HeapSize = len(heap)   # 将堆的长度当独拿出来方便
    for i in range((HeapSize - 2) // 2, -1, -1):  # 从后往前出数
        MAX_Heapify(heap,HeapSize,i)


def HeapSort(heap):  # 将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调整过程。
    Build_MAX_Heap(heap)
    for i in range(len(heap)-1,-1,-1):
        heap[0],heap[i] = heap[i],heap[0]
        MAX_Heapify(heap, i, 0)
    return heap


if __name__ == '__main__':
    a = [30, 50, 57, 77, 62, 78, 94, 80, 84]
    print(a)
    HeapSort(a)
    print(a)
    b = [random.randint(1, 1000) for i in range(1000)]
    print(b)
    HeapSort(b)
    print(b)