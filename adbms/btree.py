from BTrees.IIBTree import IIBTree
from time import time
t = IIBTree()

insertion_start_time = time()
for i in range(100000):
    t.update({i: 2*i})
insertion_end_time = time()
print("Insertion time:", format(
    (insertion_end_time-insertion_start_time)*1000, '.5f'), " milliseconds")
key = int(input("enter key: "))
search_start_time = time()

if t.has_key(key):
    print("Value", t[key])

search_end_time = time()
print("Search time:", format(
    (search_end_time-search_start_time)*1000, '.5f'), " milliseconds")
