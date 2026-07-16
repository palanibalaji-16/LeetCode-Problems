class Solution:
    def firstPalindrome(self, w: List[str]) -> str:
        c=True
        for i in w:
            a=i[::-1]
            print(a)
            if a==i and c:
                c=False
                return i
        

        return ""

        
