def unique_month(month, possible_birthdays):
	num=0
 for i in possible_birthdays:
		if month==i[0]:
			num=num+1
 if num==1:
		return True
 else:
		return False