int largestAltitude(int* gain, int gainSize) {
    int max = 0, g = 0;
    for(int i = 0; i < gainSize; i++){
        g += gain[i];
        if(max < g){
            max = g;
        }
    }   
    return max;
}