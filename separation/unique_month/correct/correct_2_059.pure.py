def unique_month(month, possible_birthdays):
    count = 0
    for x in possible_birthdays:
      if month == x[0]:
        count += 1
    if count == 1:
      return True
    else:
      return False