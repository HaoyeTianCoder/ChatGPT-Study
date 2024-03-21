def contains_unique_day(month, possible_birthdays):
	days_in_month = ()
 days_not_in_month = ()
 unique_days = ()
 for row in possible_birthdays:
		if row[0] == month:
			days_in_month = days_in_month + (row[1],)
  else:
			days_not_in_month = days_not_in_month + (row[1],)
 for row2 in days_in_month:
		if row2 in days_not_in_month:
			continue
  else:
			unique_days = unique_days + (row2,)
 if unique_days == ():
		return False
 else:
		return True