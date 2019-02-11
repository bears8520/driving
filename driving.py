country = input('請問你是哪國人：')
age = int(input('請輸入年齡：'))
if country == '台灣':
	if age >= 18:
		print('你可以開車')
	else:
		print('你還不能開車')
elif country == '美國':
	if age >= 16:
		print('你可以開車')
	else:
		print('你還不能開車')
else:
	print('你只能輸入台灣或美國')