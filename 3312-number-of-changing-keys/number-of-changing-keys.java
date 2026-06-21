class Solution {
    public int countKeyChanges(String s) {
        int  k = 0;
        String ns = s.toLowerCase();
        for(int i = 0; i < ns.length() - 1; i++){
            if(ns.charAt(i) != ns.charAt(i+1)){ k++;}
        }
        return k;
    }
}
