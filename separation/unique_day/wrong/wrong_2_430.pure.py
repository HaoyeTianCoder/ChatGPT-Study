def unique_day(day, possible_birthdays):
	unique_num = 0
 for i in possible_birthdays:
		if i[1] == day:
			unique_num = unique_num + 1
  else:
			unique_num= unique_num + 0
 if unique_num > 1:
		return False
 else:
		return True