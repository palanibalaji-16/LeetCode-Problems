class Solution:
    def checkRecord(self, s: str) -> bool:
        count =0
        lcount=0
        for i in range(len(s)):
            if s[i]=='A':
                count+=1
            if i<len(s)-2 and s[i]=='L' and s[i+1]=='L' and s[i+2]=='L':
                lcount+=1
        if count>1 or lcount>=1:
            return False
        else:
            return True
