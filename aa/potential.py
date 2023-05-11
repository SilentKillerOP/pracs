class DynamicTable:
    def __init__(self):
        self.table = [None] * 1  # Initial size of the table
        self.size = 0  # Number of elements currently in the table
        self.potential = 0  # Potential value

    def insert(self, item):
        if self.size == len(self.table):
            self.resize_table()  # Double the size of the table if it becomes full

        self.table[self.size] = item
        self.size += 1
        self.potential = len(self.table) - self.size  # Update the potential value

    def resize_table(self):
        new_table = [None] * (2 * len(self.table))  # Double the size of the table
        for i in range(self.size):
            new_table[i] = self.table[i]
        self.table = new_table

    def get_table_size(self):
        return len(self.table)

    def get_number_of_elements(self):
        return self.size

    def get_potential(self):
        return self.potential

    def get_amortized_cost(self):
        return 1 + self.potential


# Example usage
table = DynamicTable()
for i in range(100):
  table.insert(1)
  print("Table size:", table.get_table_size())
  print("Number of elements:", table.get_number_of_elements())
  print("Potential:", table.get_potential())
  print("Amortized cost:", table.get_amortized_cost())
