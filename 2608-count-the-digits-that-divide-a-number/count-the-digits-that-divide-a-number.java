class Solution {
    public int countDigits(int num) {
        int r = 0, res = 0, temp = num;
        while (temp > 0){
            r = temp % 10;
            res += (num % r == 0)?1:0;
            temp /= 10;
        }
        return res;
    }
}