x = 0
while True:
	password = input('請輸入密碼: ')
	if password == 'a123456':
		print('成功')
		break
	else:
		print('密碼輸入錯誤', '還有', 2 - x, '次機會')
		x = x + 1
		if x == 3:
			break
			
			
