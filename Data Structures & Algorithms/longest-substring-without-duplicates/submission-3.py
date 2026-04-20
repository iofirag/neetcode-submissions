class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub = 0
        unique = set()
        start = 0

        for i in range(len(s)):
            if s[i] in unique:
                max_sub = max(max_sub, len(unique))
                chIndex = s[start:i-1].find(s[i])
                start += chIndex
                unique = set(list(s[start:i]))
            unique.add(s[i])

        return max(max_sub, len(unique))
