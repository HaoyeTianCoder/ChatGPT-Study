def unique_day(day, possible_birthdays):
	check = 0
 for birthday in possible_birthdays:
		if birthday[1] == day:
			check = check + 1
 if check > 1 :
		return False
 else:
		return True