'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        temp = []
        while nums1 and nums2:
            if nums1[0] < nums2[0]:
                temp.append(nums1.pop(0))
            else:
                temp.append(nums2.pop(0))

        if nums1:
            temp.extend(nums1)
        if nums2:
            temp.extend(nums2)

        l = len(temp)
        if l%2 == 0:
            return (temp[l//2-1]+temp[l//2])/2
        else:
            return temp[l//2]




s = Solution()
l1 = [1,3]
l2 = [2,3,4,5,6,7]
print(s.findMedianSortedArrays(l1,l2))
