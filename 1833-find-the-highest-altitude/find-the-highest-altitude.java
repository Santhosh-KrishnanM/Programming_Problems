class Solution {
    public int largestAltitude(int[] gain) {
        int max = 0, g = 0;
        for(int i = 0; i < gain.length; i++){
            g += gain[i];
            if(max < g){
                max = g;
            }
        }   
        return max;
    }
}