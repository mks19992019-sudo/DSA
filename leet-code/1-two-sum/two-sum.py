class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans =[]
        hashh ={}

        for i in range(len(nums)):
            val = target - nums[i]
            if val in hashh:
                ans.append(i)
                ans.append(hashh[val])
                break
            else:
                hashh[nums[i]] = i
        return ans

        