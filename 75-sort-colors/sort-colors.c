void sortColors(int* nums, int numsSize) {
    int i, t, min, j;
    for(i = 0; i < numsSize - 1 ; i++){
        min = i;
        for(j = i + 1; j < numsSize; j++){
            if(nums[min] > nums[j]){
                min = j;
            }
        }        
        t = nums[min];
        nums[min] = nums[i];
        nums[i] = t;        
    }
}