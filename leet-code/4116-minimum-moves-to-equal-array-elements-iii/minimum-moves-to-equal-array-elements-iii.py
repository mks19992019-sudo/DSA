class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_elment = max(nums)
        count =0
        for i in nums:
            count += max_elment -i
        return count

        