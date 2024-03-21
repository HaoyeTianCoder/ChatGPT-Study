def unique_month(month, possible_birthdays):
	unique_num = 0
 for i in possible_birthdays:
		if i[0] == month:
			unique_num = unique_num + 1
  else:
			unique_num= unique_num + 0
 if unique_num > 1:
		return False
 else:
		return True