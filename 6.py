a = 1
b = 1
n = input()
n = int(n)
i = 2
while i < n:
	fib_s = a + b 
	a  = b
	b = fib_s
	i += 1
	print(fib_s)