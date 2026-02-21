int climbStairs(int n) {
    if (n <= 3) return n;
    int x = 3, y = 2, steps = 0, i = 3;
    while(i < n){
        steps = x + y;
        y = x;
        x = steps;
        i++;
    }
    return steps;
}