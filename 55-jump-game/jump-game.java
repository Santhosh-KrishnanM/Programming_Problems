class Solution {
    public boolean canJump(int[] nums) {
        int steps = nums.length - 1;
        for(int i = nums.length - 1; i>= 0; i--){
            if( i + nums[i] >= steps ){
                steps = i;
            }
        }
        return steps == 0;
    }
}