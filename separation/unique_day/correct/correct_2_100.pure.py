def unique_day(day, possible_birthdays):
    count = 0
    for x in possible_birthdays:
      if day == x[1]:
        count += 1
    if count == 1:
      return True
    else:
      return False