class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        l = 0
        # length = 0
        replacements = 0
        maxsub = 0
        # sub = set()

        for i in range(len(s)):
            if not s[i] in seen:
                seen[s[i]] = 0
            seen[s[i]] += 1

            # maxfreq = max([val for val in seen.values()])
            # repfreq = sum([val for val in seen.values()]) - maxfreq
            
            while l < i:
                maxfreq = max([val for val in seen.values()])
                repfreq = sum([val for val in seen.values()]) - maxfreq
                totalfreq = sum([val for val in seen.values()])
                if repfreq > k:
                    seen[s[l]] -= 1
                    l += 1
                else:
                    # replacements = max(replacements, i-l)
                    maxsub = max(maxsub, totalfreq)
                    break
        return maxsub