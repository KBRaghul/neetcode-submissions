import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse = ""
        dup = ""
        for i in range(len(s)):
            if s[i].isalnum():
                dup = dup + s[i]
        reverse = dup[::-1]
        return reverse.lower() == dup.lower()

        