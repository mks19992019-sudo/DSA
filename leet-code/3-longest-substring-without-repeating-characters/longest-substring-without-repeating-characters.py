class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        max_len = 0
        dist = {}
        last =0

        for i in range(len(s)):

            if s[i] in dist and (i-length)<=dist[s[i]]:
                
                l = dist[s[i]]

                
                length = (i -l)
                dist[s[i]] = i

                
            else:
                dist[s[i]] = i
                length +=1

            max_len = max(max_len,length)
        return max_len




        