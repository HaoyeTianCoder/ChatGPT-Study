def contains_unique_day(month, possible_birthdays):
    collect=()
    for i in possible_birthdays:
      if i[0]==month:
        collect+=(i[1],)
    for i in collect:
      if unique_day(i,possible_birthdays):
        return True
    return False