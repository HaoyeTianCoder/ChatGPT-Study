def contains_unique_day(month, possible_birthdays):
    a = ()
    b = False
    for i in possible_birthdays:
        if month == i[0]:
            a += (i,)
    for i in a:
        b = b or unique_day(i[1], possible_birthdays)
    return b