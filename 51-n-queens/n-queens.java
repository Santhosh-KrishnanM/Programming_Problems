class Solution {
    char[][] res;
    List<List<String>> out;
    Set<Integer> cols;
    Set<Integer> diag1;
    Set<Integer> diag2;
    int n;
    public List<List<String>> solveNQueens(int n) {
        this.out = new ArrayList<>();
        this.res = new char[n][n];
        this.n = n;
        for(int i = 0; i < n; i++){
            Arrays.fill(res[i], '.');
        }
        this.cols = new HashSet<>();
        this.diag1 = new HashSet<>();
        this.diag2 = new HashSet<>();
        backtrack(0);
        return out;
    }
    public void backtrack(int row){
        if(row == n){
            out.add(constructBoard());
            return;
        }
        for(int col = 0; col < n; col++){
            int d1 = row - col;
            int d2 = row + col;
            if(cols.contains(col) || diag1.contains(d1) || diag2.contains(d2)){
                continue;
            }
            cols.add(col);
            diag1.add(d1);
            diag2.add(d2);
            res[row][col] = 'Q';
            backtrack(row + 1);

            cols.remove(col);
            diag1.remove(d1);
            diag2.remove(d2);
            res[row][col] = '.';
        }
    }

    public List<String> constructBoard(){
        List<String> board = new ArrayList<>();
        for(int i = 0; i < n; i++){
            board.add(new String(res[i]));
        }
        return board;
    }
}