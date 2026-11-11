class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        arr2.sort()
        count = 0
        for x in arr1:
            left = x - d
            right = x + d

            start = 0
            end = len(arr2) - 1
            while start <= end:
                mid = (start + end) // 2

                if arr2[mid] < left:
                    start = mid + 1
                else:
                    end = mid - 1
            if start == len(arr2) or arr2[start] > right:
                count += 1

        return count