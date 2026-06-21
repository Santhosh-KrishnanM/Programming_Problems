class Solution {
    public int calPoints(String[] operations) {
        ArrayList<Integer> arr = new ArrayList<>();
        for(String c : operations){
            int n = arr.size();
            if(c.equals("C")){
                arr.remove(n-1);
            }else if(c.equals("D")){
                arr.add(arr.get(n - 1) * 2);
            }else if(c.equals("+")){
                arr.add(arr.get(n - 1) + arr.get(n - 2));
            }else{
                arr.add(Integer.parseInt(c));
            }
        }
        int sum = 0;
        for(int i = 0; i < arr.size(); i++){
            sum += arr.get(i);
        }
        return sum;
    }
}