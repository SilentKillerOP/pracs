nodes = { "a" : ['b','c'] , "b":['d'] , "c":['e'] ,"d":['a'] , 'e':['f']}
v = set()
o = []
def dfs(key , i):
    o.append(i)
    if key == i:
        v.add(i)
        return [i]
    else: 
        v.add(i)
        for j in nodes[i] :
            if j not in v:
                dfs(key,j)
        return o 
ans = dfs("f",'a')
print("Sequence : " ,end = "")
for i in ans:
    print(i , end=" ")
