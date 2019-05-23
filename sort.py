# https://mp.weixin.qq.com/s/vn3KiV-ez79FmbZ36SX9lg



def bubble_sort(l):
    '''
    时间复杂度 （n-1）+ (n-2) + (n-3) + ... + 1 = n*(n-1)/2
    O(n^2)
    :param l:
    :return:
    '''
    length = len(l)
    if length == 0 or length == 1:
        return l

    for i in range(length-1):
        for j in range(i+1,length):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]

    return l


def selection_sort(l):
    '''
    时间复杂度 n-1）+ (n-2) + (n-3) + ... + 1 = n*(n-1)/2
    O(n^2)
    :param l:
    :return:
    '''
    length = len(l)
    if length == 0 or length == 1:
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
    :param l:
    :return:
    '''
    length = len(l)
    if length == 0 or length == 1:
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
    test
    :param l:
    :return:
    '''
    length = len(l)
    if length == 0 or length == 1:
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



if __name__ == '__main__':
    l1 = [9, 8, 6, 7, 6, 5, 3, 4, 2, 1]
    l2 = [1]
    l3 = []
    l0 = shell_sort(l1)
    print(l0)

