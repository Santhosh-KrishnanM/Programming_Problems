class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        def computeGCD(x, y):
            while(y):
                x, y = y, x % y
            return x
        
        dm = {i:{j for j in range(51) if computeGCD(i,j) == 1} for i in range(51)}
        
        ed = defaultdict(list)
        ans = [-1]*len(nums)
        for x,y in edges:
            ed[x].append(y)
            ed[y].append(x)
        
        done = set()
        stack = deque([(0,{})])
        lvl = 0
        while stack:
            sl = len(stack)
            for _ in range(sl):
                node, parents  = stack.popleft()
                overlap = dm[nums[node]] & parents.keys()
                if overlap:
                    ans[node] = parents[max(overlap, key=lambda x: parents[x][1])][0]
                done.add(node)
                for child in ed[node]:
                    if child not in done:
                        np = parents.copy()
                        np[nums[node]] = (node, lvl)
                        stack.append((child, np ))
            lvl += 1
            
        return ans