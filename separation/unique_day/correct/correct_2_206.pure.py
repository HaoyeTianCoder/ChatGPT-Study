def unique_day(date, possible_birthdays):
    uniqueday = ()
    days = ()
    for i in possible_birthdays:
        days += (i[1],)
    for i in days:
        if i == date:
            uniqueday += (i,)
        else:
            continue
    if len(uniqueday) == 1:
        return True
    else:
        return False