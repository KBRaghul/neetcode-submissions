import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse = ""
        for i in range(len(s) - 1, -1, -1):
            if s[i].isalnum():
                reverse = reverse + s[i]
        dup = ""
        for i in range(len(s)):
            if s[i].isalnum():
                dup = dup + s[i]
        print(dup)
        return reverse.lower() == dup.lower()

        