class Solution {
    public int subtractProductAndSum(int n) {
        int p = 1,s = 0;
        int r;
        while(n > 0){
            r = n % 10;
            p *= r;
            s += r;
            n /= 10;
        }
        int res = p - s;
        return res;
    }
}