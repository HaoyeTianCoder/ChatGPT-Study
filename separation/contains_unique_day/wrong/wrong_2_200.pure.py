def contains_unique_day(month, possible_birthdays):
    uniquedays = ()
    daysinmonth = ()
    for i in possible_birthdays:
        if unique_day(i[1], possible_birthdays)== True:
            uniquedays += (i[1],)
    for i in possible_birthdays:
        if i[0] == month:
            daysinmonth += (i[1],)
    for each in uniquedays:
        if each in daysinmonth:
            return True
        else:
            continue
    return False