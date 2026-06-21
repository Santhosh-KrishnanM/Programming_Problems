class Solution {
    public int mostWordsFound(String[] sentences) {
        int n = sentences.length;
        int max = 0, c;
        for(int i = 0; i < n; i++){
            c = 0;
            String[] wc = sentences[i].trim().split("\\s+");
            if(max < wc.length){
                max = wc.length;
            }
        }
        return max;
    }
}