import random
s = int(input("Введите количество конфет: "))
n= int(input("Введите максимальное количество конфет при одном ходе игрока: "))
d = {1:"Первый",-1:"Второй"}
k=1
while s > n:
	minus = random.randint(1,n)
	if k==1:
		minus = s%(n+1)
	s=s-minus
#	print (d[k], minus)
	k=-k
	if s<=n:
		print (f"{d[k]} победил, {s} конфет осталось")
	