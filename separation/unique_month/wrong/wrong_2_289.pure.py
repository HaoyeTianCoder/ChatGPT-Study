def unique_month(month, possible_birthdays):
    a = ()
    for i in possible_birthdays:
        a += (i[1],)
    return a.count(month) == 1