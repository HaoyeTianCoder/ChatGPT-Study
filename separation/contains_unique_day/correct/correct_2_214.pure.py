def contains_unique_day(month, possible_birthdays):
	return len(tuple(filter(lambda x: unique_day(x[1], possible_birthdays), 
  filter(lambda y: y[0] == month, possible_birthdays)))) > 0