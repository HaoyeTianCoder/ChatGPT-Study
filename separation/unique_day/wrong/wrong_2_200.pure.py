def unique_day(day, possible_birthdays):
    total = ()
    for i in possible_birthdays:
        total += (i[1],)
    if total.count(day) > 1: 
        return False
    else:
        return True