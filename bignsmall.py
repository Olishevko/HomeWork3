a = int(input('first number: '))  # ввод , ввывод трех значений
b = int(input('second number: '))
c = int(input('third number: '))
if a > b and a > c:  #исключение большего числа 
	maxn = a
elif b > a and b > c:
	maxn = b
else:
	maxn = c
if a < b and a < c:  # исключение меньшего числа
	minn = a
elif b < a and b < c:
	minn = b
else:
	minn = c
print(maxn, minn)
