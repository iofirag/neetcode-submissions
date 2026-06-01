class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 0
        r = len(digits) -1

        while r >= 0:
            if digits[r] == 9:
                digits[r] = 0
                carry = 1
                r -= 1
            else:
                digits[r] += 1
                carry = 0
                break
                
        if carry:
            return [1] + digits
        return digits