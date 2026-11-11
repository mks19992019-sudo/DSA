class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_el = nums[0]
        total_count = 0

        for i in range(1,len(nums)):
            if max_el > nums[i]:
                total_count += max_el - nums[i]
            else:
                count = nums[i] - max_el
                max_el = nums[i]

                total_count += count*(i)
        return total_count
                


        
        