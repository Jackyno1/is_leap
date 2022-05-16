# 檢驗是否閏年
while True: 

	year = input('請問此年是否為閏年?(按q離開)')

	if year == 'q':
		break

	year = int(year)

	def is_leap(year):
		if year % 4 != 0:
			return False
		elif year % 100 != 0:
			return True
		elif year % 400 != 0:
			return False
		elif year % 3200 != 0:
			return True
		else:
			return False

	print(is_leap(year))
