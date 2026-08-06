class Solution:
    
    def valid(self, char: str) -> bool:
        valid_chars = [('0', '9'), ('a', 'z'), ('A', 'Z')]

        for l, r in valid_chars:
            if l <= char <= r:
                return True
        return False

    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) - 1

        while p1 < p2:
            if not self.valid(s[p1]):
                p1 += 1
                continue

            if not self.valid(s[p2]):
                p2 -= 1
                continue

            if s[p1].lower() != s[p2].lower():
                return False

            p1 += 1
            p2 -= 1

        return True

 