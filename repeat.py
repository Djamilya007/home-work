def roots(a = 1, b = 1, c = 2):
	D = b*b - 4*a*c 
	if D < 0:
		print('Нет действительных корней') 
		return
	elif D == 0:
		print('Два совпадающих корня')
		x1 = -b/(2*a)
		return x1
	else:
		print('Два различных корня')
		x1 = (-b+D**0.5)/(2*a)
		x2 = (-b-D**0.5)/(2*a)
		return x1, x2
		
x1, x2 = roots(1,2,0)
print(x1,x2)