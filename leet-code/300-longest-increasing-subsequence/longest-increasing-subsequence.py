class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        temp =[]

        for i in nums:

            if not temp or i>temp[-1]:
                temp.append(i)
            else:
                left = 0
                right = len(temp) - 1
                while left < right:
                    mid = (left+right)//2

                    if temp[mid] < i:
                        left = mid +1
                    else:
                        right = mid
                
                temp[left] =i
        return len(temp)

       
        
        