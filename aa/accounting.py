import time 
import random
bank = 0
ccost = 3
cost = 0 
def multipop(stck,n):
    global cost
    for i in range(n):
      stck.pop()
    return stck

def mstck(stck):
  global cost 
  cost = 0
  s = []
  for i in stck:
    if i <= len(s):
      s = multipop(s , i)
    s.append(i)
    bank+= ccost - cost
    print(i , s , cost)

ar = [random.randint(1,10) for i in range(10)]
print(ar)
mstck(ar)

print(" Amortize cost:" , cost ,'\n' , "Asymptotic cost:" , len(ar)**2)
