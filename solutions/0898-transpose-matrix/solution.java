class Solution {
    public int[][] transpose(int[][] m) {
        int l=m[0].length;
        int k=m.length;
        int[][] r=new int[l][k];
        for(int i =0;i<k;i++){
            for (int j=0;j<l;j++){
                r[j][i]=m[i][j];
            }
        }
        return r;
    }
}
