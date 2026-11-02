class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        preMap = {i: [] for i in range(n)}
        visit = set()

        for n1, n2 in edges:
            preMap[n1].append(n2)
            preMap[n2].append(n1)
        
        def dfs(e, prev):
            if e in visit:
                return False
            
            visit.add(e)
            for node in preMap[e]:
                if node == prev:
                    continue
                if not dfs(node, e):
                    return False
            return True
        
        
        return dfs(0, -1) and n == len(visit)