def unique_day(day, possible_birthdays):
	return len(tuple(filter(lambda y: day == y, 
 map(lambda x: x[1], possible_birthdays)))) == 1