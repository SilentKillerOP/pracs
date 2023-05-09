import math 

class DynamicTable:
  def __init__(self, capacity=1):
    self.table = [0] * capacity
    self.size = 0
    self.capacity = capacity
  def add(self, element):
    if self.size == self.capacity:
    # Double the capacity of the table if it is full
      new_table = [0] * (self.capacity * 2)
      for i in range(self.size):
        new_table[i] = self.table[i]
        self.table = new_table
        self.capacity *= 2
        # print(f"Table doubled, new size: {self.capacity}")
      self.table.append(element)
      self.size += 1
    def size(self):
      return self.size
  def capacity(self):
    return self.capacity
  def numDoublings(self):
  # Calculate the number of times the table was doubled
    return int(math.log2(self.capacity))
  def numCopyings(self):
  # Calculate the number of times elements were copied during resizing
    num_copyings = 0
    for i in range(1, self.numDoublings() + 1):
      num_copyings += 2**(i-1)
    return num_copyings
table = DynamicTable()
cost = 0
f = 0
operation_cost = 1
print("Item No\tTable Size\tTable Cost\tCost of Operation")
print("=====================================================")
for i in range(1, 18):
  table.add(i)
  if f == 1:
    cost = table.size
    f = 0
  else:
    cost = 1
  if table.size == table.capacity:
    f = 1
  print(f"{i}\t{table.capacity}\t\t{cost}\t\t\t{operation_cost}")