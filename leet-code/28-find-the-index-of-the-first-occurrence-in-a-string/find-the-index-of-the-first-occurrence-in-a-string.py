class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_n = len(needle)
        for i in range(len(haystack)-len_n+1):
            if haystack[i:i+len_n] == needle:
                return i
        return -1
        