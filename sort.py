# https://mp.weixin.qq.com/s/vn3KiV-ez79FmbZ36SX9lg
# https://www.cnblogs.com/zhaoyingjie/p/6266011.html

def bubble_sort(l):
    '''
    时间复杂度 （n-1）+ (n-2) + (n-3) + ... + 1 = n*(n-1)/2
    O(n^2)
    空间复杂度 O(1)
    '''
    length = len(l)
    if length < 2:
        return l

    for i in range(length-1):
        for j in range(length-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

    return l


def selection_sort(l):
    '''
    时间复杂度 n-1）+ (n-2) + (n-3) + ... + 1 = n*(n-1)/2
    O(n^2)
    空间复杂度 O(1)
    '''
    length = len(l)
    if length < 2:
        return l

    for i in range(length-1):
        minIndex = i
        for j in range(i+1,length):
            if l[minIndex] > l[j]:
                minIndex = j
        if minIndex != i:
            l[minIndex], l[i] = l[i],l[minIndex]
    return l

def insert_sort(l):
    '''
    将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
    从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
    时间复杂度：1+2+3+...+(n-1) = n*(n-1)/2
    O(n^2)
    空间复杂度 O(1)
    '''
    length = len(l)
    if length < 2:
        return l

    for i in range(1,length):
        j = i-1
        # key是未排序序列的最后一个元素
        key = l[i]
        while j >= 0:
            if key < l[j]:
                l[j+1] = l[j]
                l[j] = key
            j -= 1
    return l

def shell_sort(l):
    '''
    希尔排序/缩小增量排序
    先将整个待排记录序列分割成若干个子序列分别进行直接插入排序，带整个序列中的记录基本有序时，再对全体记录进行一次直接插入排序
    希尔排序平均效率是O(nlogn)，大概是O(n^1.3)。其中分组的合理性会对算法产生重要的影响
    空间复杂度 O(1)
    '''
    length = len(l)
    if length < 2:
        return l

    # gap = 1
    # while gap < length/3:
    #     gap = gap*3+1
    gap = length//2

    while gap > 0:
        for i in range(gap,length):
            tmp = l[i]
            j = i-gap
            while j >= 0 and l[j] > tmp:
            # 插入排序
                l[j+gap] = l[j]
                j -= gap
            l[j+gap] = tmp
        gap = gap//2
    return l


def shell_sort_2(l):
    length = len(l)
    if length < 2:
        return l

    gap = length // 2

    while gap > 0:
        # 这部分代码完全来源于插入排序，唯一区别就是把1替换成gap
        for i in range(gap, length):
            key = l[i]
            j = i - gap
            while j >= 0:
                if l[j] > key:
                    l[j + gap] = l[j]
                    l[j] = key
                j -= gap
        gap = gap // 2
    return l

def merge_sort(l):
    '''
    归并排序：归并排序法是将两个或以上的有序表合并成一个新的有序表，即把待排序序列分成若干个子序列，每个子序列是有序的。然后再把有序子序列合并为整体
    有序序列。注意：一定要是有序序列！
    时间复杂度：O(nlogn)
    推导 https://blog.csdn.net/qq_31617121/article/details/79249546
    递归树推导，每一层树的时间复杂度都是O(n)，共有logn层
    空间复杂度 O(n)
    '''
    length = len(l)
    if length < 2:
        return l
    middle =length//2
    left = l[:middle]
    right = l[middle:]
    return merge(merge_sort(left),merge_sort(right))

def merge(left,right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left:
        result.extend(left)
    if right:
        result.extend(right)

    return result

def quick_sort(l,left,right):
    '''
    设置两个指针low和high，他们的初值分别是l[low], l[high]。设枢轴关键字为key，首先从high位置起向前搜索找到第一个关键字小于key的记录，进行
    交换，然后从low位置起向后搜索找到第一个关键字大于key的记录，进行交换，重复这两步直至low == high。
    :param l:
    :param left:
    :param right:
    :return:
    '''
    length = len(l)
    if length < 2:
        return l
    if left >= right:
        return l
    low, high = left, right
    key = l[left]
    while left < right:
        while left < right and key <= l[right]:
            right -= 1
        l[left] = l[right]
        while left < right and key >= l[left]:
            left += 1
        l[right] = l[left]
    l[right] = key
    print(l)
    quick_sort(l,low,left-1)
    quick_sort(l,left+1,high)
    return l


if __name__ == '__main__':
    l1 = [9, 8, 6, 7, 6, 5, 3, 4, 2, 1]
    l2 = [1]
    l3 = []
    l4 = [49, 38, 65, 97, 76, 13, 27, 49]
    l0 = quick_sort(l4, 0, len(l4) - 1)
    print(l0)

