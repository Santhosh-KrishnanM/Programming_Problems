class Solution {
    public int[] getConcatenation(int[] nums) {
        int n = nums.length, i;
        int[] arr = new int[n*2];
        for(i = 0; i < n; i++){
            arr[i] = nums[i];
        }
        for(i = n; i < n*2; i++){
            arr[i] = nums[i-n];
        }
        return arr;
    }
}