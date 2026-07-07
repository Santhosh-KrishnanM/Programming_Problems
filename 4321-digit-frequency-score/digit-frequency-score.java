class Solution {
    public int digitFrequencyScore(int n) {
        int d = 0;
        while (n > 0){
            int r = n % 10;
            d += r;
            n /= 10;
        }
        return d;
    }
}
/*d = 0
        while n > 0:
            r = n % 10
            d += r
            n //= 10
        return d*/