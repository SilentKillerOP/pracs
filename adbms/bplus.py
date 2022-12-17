from bplustree import BPlusTree
from time import time

t = BPlusTree('/bplustre.db', order= 50)
st = time()
for i in range(1000):
    c = i.to_bytes(10, 'big')
    t[i]=c
et = time()

print("Insertion time:", format((et-st)*1000, '.5f'), " milliseconds")
key = int(input("Enter Key:"))

st = time()
data = t.get(key)
et = time()

data = int.from_bytes(data, 'big')
print("Search time:", format((et-st)*1000, '.5f'), " milliseconds")