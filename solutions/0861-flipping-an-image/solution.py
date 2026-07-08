class Solution:
    def flipAndInvertImage(self, ima: List[List[int]]) -> List[List[int]]:
        k=[]
        for i in ima:
            i.reverse()
        for i in range(len(ima)):
            for j in range(len(ima[0])):
                if ima[i][j]==1:
                    ima[i][j]=0
                else:
                    ima[i][j]=1
        
        return ima


        

