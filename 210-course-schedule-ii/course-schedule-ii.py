class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {c:[] for c in range(numCourses)}
        for crs, pre in  prerequisites:
            premap[crs].append(pre)

        res = []
        visited , cycle = set() , set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            for pre in premap[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return res

