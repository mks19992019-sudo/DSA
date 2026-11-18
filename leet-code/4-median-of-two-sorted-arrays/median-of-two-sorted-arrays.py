class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        i = 0
        j = 0

        m = len(nums1)
        n = len(nums2)
        ans = []

        while i < m and j < n:
            if nums1[i] > nums2[j]:
                ans.append(nums2[j])
                j+=1
            else:
                ans.append(nums1[i])
                i+=1
        
        if i < m:
            ans.extend(nums1[i:])
        else:
            ans.extend(nums2[j:])
        
        n_ = len(ans)

        if n_ % 2 == 0:
            median = (ans[(n_//2)] + ans[(n_//2)-1])/2
            return median
        else:
            return ans[(n_//2)]




     


        

        

        