class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for word in strs:
            word_sorted = str("".join(sorted(word)))
            
            if word_sorted not in anagram_map:
                anagram_map[word_sorted] = []

            anagram_map[word_sorted].append(word)
        
        # list each key-values of anagram_map to list of groups
        return [val for k, val in anagram_map.items()]