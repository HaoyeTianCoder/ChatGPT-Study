def unique_month(month, possible_birthdays):
	check = 0
 for birthday in possible_birthdays:
		if birthday[0] == month:
			check = check + 1
 if check > 1 :
		return False
 else:
		return True