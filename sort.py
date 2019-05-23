# https://mp.weixin.qq.com/s/vn3KiV-ez79FmbZ36SX9lg
# https://www.cnblogs.com/zhaoyingjie/p/6266011.html

def bubble_sort(l):
    '''
    时间复杂度 （n-1）+ (n-2) + (n-3) + ... + 1 = n*(n-1)/2
    空间复杂度 O(1)
    O(n^2)
    :param l:
    :return:
    '''
    length = len(l)
    if length < 2:
        return l

    for i in range(length-1):
        for j in range(i+1,length):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]

    return l


def selection_sort(l):
    '''
    时间复杂度 n-1）+ (n-2) + (n-3) + ... + 1 = n*(n-1)/2
    空间复杂度 O(1)
    O(n^2)
    :param l:
    :return:
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
    :param l:
    :return:
    '''
    length = len(l)
    if length < 2:
        return l

    for i in range(1,length):
        j = i-1
        key = l[i]
        while j >= 0:
            if key < l[j] :
                l[j+1] = l[j]
                l[j] = key
            j -= 1
    return l

def shell_sort(l):
    '''
    希尔排序/缩小增量排序
    希尔排序平均效率是O(nlogn)，大概是O(n^1.3)。其中分组的合理性会对算法产生重要的影响
    空间复杂度 O(1)
    :param l:
    :return:
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

def merge_sort(l):
    '''
    归并排序：归并排序法是将两个或以上的有序表合并成一个新的有序表，即把待排序序列分成若干个子序列，每个子序列是有序的。然后再把有序子序列合并为整体
    有序序列。注意：一定要是有序序列！
    时间复杂度：O(nlogn)
    推导 https://blog.csdn.net/qq_31617121/article/details/79249546
    递归树推导，每一层树的时间复杂度都是O(n)，共有logn层
    空间复杂度 O(n)
    :param l:
    :return:
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

if __name__ == '__main__':
    l1 = [9, 8, 6, 7, 6, 5, 3, 4, 2, 1]
    l2 = [1]
    l3 = []
    l0 = merge_sort(l1)
    print(l0)

