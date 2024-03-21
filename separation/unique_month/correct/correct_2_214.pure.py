def unique_month(month, possible_birthdays):
	return len(tuple(filter(lambda y: month == y, 
 map(lambda x: x[0], possible_birthdays)))) == 1