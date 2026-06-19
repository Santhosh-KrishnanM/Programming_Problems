class Solution {
    public String triangleType(int[] nums) {
        int n = nums.length;
        int c = 0, r = 1;
        if(nums[0] + nums[1] <= nums[2]){
            r = 0;
        } if(nums[0] + nums[2] <= nums[1]){
            r = 0;
        } if(nums[1] + nums[2] <= nums[0]){
            r = 0;
        }
        if(r == 0){
            return "none";
        }
        HashSet<Integer> arr = new HashSet<>();
        for(int i = 0; i < n; i++){
            arr.add(nums[i]);
        }
        int l = arr.size();
        if (l == 1){
            return "equilateral";
        }else if (l == 2){
            return "isosceles";
        }else{
            return "scalene";
        } 
    }
}