class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        total = float('inf')
        flag = True

        for k_size in range(l,r+1):

            for i in range(len(nums)-k_size+1):
                curen_sum = sum(nums[i:i+k_size])
                if curen_sum > 0:
                    total = min((total,curen_sum))
                
        if total == float('inf'):
            return -1      
        return total

      