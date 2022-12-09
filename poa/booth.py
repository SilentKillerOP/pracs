from bitstring import BitArray

def booth(m, r, x, y):
	totalLength = x + y + 1
	A = BitArray(int = m, length = totalLength) << (y+1)
	S = BitArray(int = -m, length = totalLength)  << (y+1)
	M = BitArray(int = r, length = y)
	M.prepend(BitArray(int = 0, length = x))
	M = M << 1
	print ("Initial values")
	print ("A", A.bin)
	print ("S", S.bin)
	print ("P", M.bin)
	for i in range(1,y+1):
		if M[-2:] == '0b01':
			M = BitArray(int = M.int + A.int, length = totalLength)
			print ("A +  M:", M.bin)
		elif M[-2:] == '0b10':
			M = BitArray(int = M.int +S.int, length = totalLength)
			print ("A -  M:", M.bin)
		M = right_shift(M, 1)
		print ("A >> 1:", M.bin)
	M = right_shift(M, 1)
	print ("Final value of A >> 1:", M.bin)
	return M.int

def right_shift(x, amt):
	l = x.len
	x = BitArray(int = (x.int >> amt), length = l)
	return x

# Sample usage: find 86 * 41
b = booth(10, 5, 8, 8)
print (b)