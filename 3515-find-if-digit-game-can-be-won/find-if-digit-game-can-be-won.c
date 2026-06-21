bool canAliceWin(int* nums, int numsSize) {
    int alice = 0, bob = 0;
    for(int i = 0; i < numsSize; i++){
        if(nums[i] < 10){ alice += nums[i];}
        else{ bob += nums[i];}
    }
    return alice != bob;
}