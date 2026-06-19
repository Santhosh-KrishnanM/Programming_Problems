class Solution {
    public String toLowerCase(String s) {
        char[] arr = new char[s.length()];
        for(int i = 0; i < s.length(); i++){
            int c = s.charAt(i);
            if(c <= 'Z' && c >= 'A'){
                c += 32;
            }
            arr[i] = (char) c;
        }
        String res = String.valueOf(arr);
        return res;
    }
}