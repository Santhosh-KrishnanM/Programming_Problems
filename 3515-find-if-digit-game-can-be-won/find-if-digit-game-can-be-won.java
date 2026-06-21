class Solution {
    public boolean canAliceWin(int[] nums) {
        int alice = 0, bob = 0;
        for(int i : nums){
            if(i < 10){ alice += i;}
            else{ bob += i;}
        }
        return alice != bob;
    }
}