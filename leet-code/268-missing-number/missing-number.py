class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        sum = 0
        array_sum =0

        for i in range(len(nums)):
            sum = sum+(i+1)

            array_sum += nums[i]
        
        return (sum - array_sum)

            




        