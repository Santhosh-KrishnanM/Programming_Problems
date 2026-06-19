class Solution {
    public int differenceOfSum(int[] nums) {
        int n = nums.length;
        int res, r;
        int sum = 0;
        int dsum = 0;
        for(int i= 0; i < n; i++){
            sum += nums[i];
        }
        System.out.println(sum);
        for(int i = 0; i < n; i++){
            if(nums[i] <= 9){
                dsum += nums[i];
            }
            //System.out.println(dsum);
            else{
                while(nums[i] > 0){
                    r = nums[i] % 10;
                    dsum += r;
                    nums[i] /= 10;
                }
            }
        }
        System.out.println(dsum);
        res = sum - dsum;
        return res;
    }
}