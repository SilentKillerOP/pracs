from collections import deque
nodes = { "a" : ['b','c'] , "b":['d'] , "c":['e'] ,"d":['a'] , 'e':['f'] , 'f':['a']}
q = deque()
v = set()
def bfs(i , key):
    if i == key: return [i]
    else: 
        o = []
        q.append(i)
        v.add(i)
        while q:
            c = q.popleft()
            o+=[c]
            for j in nodes[c]:
                if j not in v:
                    v.add(j)
                    q.append(j)
                    if j == key:
                        return o
        return o
ans = bfs('a','f')
print("Sequence : " ,end = "")
for i in ans:
    print(i , end=" ")