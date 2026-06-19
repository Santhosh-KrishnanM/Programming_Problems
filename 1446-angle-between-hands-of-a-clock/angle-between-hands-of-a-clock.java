class Solution {
    public double angleClock(int hour, int minutes) {
        double M = minutes * 6;
        double H = (hour * 30) + (minutes * 0.5);
        double res = Math.abs(H - M);
        System.out.println(res);
        if (res > 180 ){
            return 360 - res;
        }
        return res;
    }
}