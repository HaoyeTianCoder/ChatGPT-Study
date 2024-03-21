def contains_unique_day(month, possible_birthdays):
  possible_days = ()
  for x in possible_birthdays:
    if x[0] == month:
      possible_days += (x,)
  for day in possible_days:
    if unique_day(day[1], possible_birthdays) == True:
      return True
  else:
    return False