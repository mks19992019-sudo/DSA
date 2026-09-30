class Solution(object):
    def maxDepthAfterSplit(self, seq):
        depth = 0
        ans = []

        for ch in seq:
            if ch == '(':
                ans.append(depth % 2)
                depth += 1
            else:
                depth -= 1
                ans.append(depth % 2)

        return ans
        