def NOD(num1, num2):
	while num1!=0 and num2!=0:
		if num1>num2:
			num1=num1%num2
		else:
			num2=num2%num1
	return 'Наибольший общий делитель:{}'.format(num1+num2)

print(NOD(int(input('Введите первое число:')), int( input('Введите второе число:'))))