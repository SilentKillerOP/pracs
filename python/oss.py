import os

path = "D:/Downloads"
d= {}
files = os.listdir(path)
for i in files:
    _ , c = os.path.splitext(i)
    if c in d:
        d[c]+=1
    else:
        d[c]=1
for i in d:
    print(i , d[i])