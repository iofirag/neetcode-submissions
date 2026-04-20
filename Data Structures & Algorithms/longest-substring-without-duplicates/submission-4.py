class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        seen = set()
        left = 0


        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, len(seen))
        return max_len
        #     if s[i] in unique:
        #         max_sub = max(max_sub, len(unique))
        #         chIndex = s[start:i-1].find(s[i])
        #         start += chIndex
        #         unique = set(list(s[start:i]))
        #     unique.add(s[i])

        return 
