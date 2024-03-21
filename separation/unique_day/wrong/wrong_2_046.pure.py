def unique_day(day, possible_birthdays):
	num=0
 for i in possible_birthdays:
		if day==i[1]:
			num=num+1
 if num==1:
		return True
 else:
		return False