def contains_unique_day(month, possible_birthdays):
    possible_days = ()
    count = 0
    for i in possible_birthdays:
        if i[0] == month:
            possible_days += (i,)
    for j in possible_days:
        day = j[1]
        if (unique_day(day, possible_birthdays) == True):
            return True
    return False