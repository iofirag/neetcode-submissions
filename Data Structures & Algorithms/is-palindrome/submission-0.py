class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove all non char between ascii of A-Z a-z 0-9
        left_i = 0
        right_i = len(s)-1
        while left_i < right_i:
            # check if both 
            if not s[left_i].isalnum():
                # char not in ascii of A-Z a-z 0-9
                left_i += 1
                continue

            if not s[right_i].isalnum():
                right_i -= 1
                continue

            if s[left_i].lower() == s[right_i].lower():
                left_i += 1
                right_i -= 1
                continue
            else:
                return False
            
        return True