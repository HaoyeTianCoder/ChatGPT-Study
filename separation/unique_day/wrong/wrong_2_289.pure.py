def unique_day(date, possible_birthdays):
    a = ()
    for i in possible_birthdays:
        a += (i[1],)
    return a.count(day) == 1