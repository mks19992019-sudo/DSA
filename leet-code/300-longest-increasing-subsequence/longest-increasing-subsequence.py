class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1]*n

        for i in range(1,n):
            dp[i] = max((dp[j] for j in range(i) if nums[j]<nums[i]),default=0) + 1
        
        return max(dp)
        
        