from collections import defaultdict

g = defaultdict(list)
def addEdge( u, v):
        g[u].append(v)

def DLS(src, target, maxDepth):
        if src == target:
            return str(src)
        if maxDepth <= 0:
            return False
        for i in g[src]:
            if(DLS(i, target, maxDepth-1)):
                return str(src)+"->"+str(i)+","+DLS(i, target, maxDepth-1)
        return False

def IDDFS(src, target, maxDepth):
        for i in range(maxDepth):
            if (DLS(src, target, i)):
                return DLS(src, target, i)
        return False



addEdge(0, 1)
addEdge(0, 2)
addEdge(1, 3)
addEdge(1, 4)
addEdge(2, 5)
addEdge(2, 6)

target = 6
maxDepth = 4
src = 0

if IDDFS(src, target, maxDepth) :
    print("Target is reachable from source " +
          "by sequence:" , end='')
    ans = IDDFS(src, target, maxDepth) 
    print(ans[:-1])
else:
    print("Target is NOT reachable from source " + "within max depth")
