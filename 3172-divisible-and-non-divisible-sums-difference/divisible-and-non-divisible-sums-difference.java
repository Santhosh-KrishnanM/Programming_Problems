class Solution {
    public int differenceOfSums(int n, int m) {
        int div_3 = 0;
        int ndiv_3 = 0, i;
        for(i = 1; i <= n; i++){
            if(i % m == 0){
                div_3 += i;
            }
            else {
                ndiv_3 += i;
            }
        }
        return ndiv_3 - div_3;
    }
}