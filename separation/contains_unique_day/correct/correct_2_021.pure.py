def contains_unique_day(month, possible_birthdays):
    possible_days = ()
    for i in possible_birthdays:
        if i[0] == month:
            possible_days += (i[1],)
    for i in possible_days:
        if unique_day(i, possible_birthdays) == True:
            return True
    return False