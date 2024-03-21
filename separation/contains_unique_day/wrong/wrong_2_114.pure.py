def contains_unique_day(month, possible_birthdays):
	for birthday in possible_birthdays:
		if month == birthday[0] and unique_day(birthday[1], possible_birthdays):
				return True
 else:
		return False