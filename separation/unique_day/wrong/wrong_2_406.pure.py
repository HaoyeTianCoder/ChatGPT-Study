def unique_day(day, possible_birthdays):
    tupleofdays = ()
    for i in possible_birthdays:
        tupleofdays += (i[1],)
    count = 0
    for i in tupleofdays:
        if day == i:
            count += 1
    return count == 1