def unique_day(day, possible_birthdays):
    count = 0
    alldays = ()
    for i in possible_birthdays:
        alldays += (i[1],)
    for i in alldays:
        if day == i:
            count += 1
    if count == 1:
        return True
    else:
        return False