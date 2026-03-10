class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Keep only letters and numbers, and make them lowercase
        # (This removes the need for .split(",") or .split(":"))
        cleaned = "".join(char.lower() for char in s if char.isalnum())

        # 2. Create the reversed version
        reversed_s = cleaned[::-1]

        # 3. Compare them
        if cleaned == reversed_s:
            return True
        else:
            return False

        
