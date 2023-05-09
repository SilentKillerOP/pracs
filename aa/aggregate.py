import time 
import random
cost = 0
def multipop(stck,n):
    global cost
    for i in range(n):
      stck.pop()
      cost+=1
    return stck

def mstck(stck):
  global cost
  s = []
  for i in stck:
    if i <= len(s):
      s = multipop(s , i)
    s.append(i)
    cost+=1
    print("Element value:",i ,',Stack:', s ,",Amortize cost:",  cost)

ar = [random.randint(1,10) for i in range(10)]
print("Array :",ar)
mstck(ar)

print("Amortize cost:" , cost ,'\n' , "Asymptotic cost:" , len(ar)**2)
