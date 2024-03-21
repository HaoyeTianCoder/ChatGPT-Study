def contains_unique_day(month, possible_birthdays):
    x = ()
    for i in possible_birthdays:
        if i[0] == month:
            x = x + (i,)
    total = 0
    for i in x:
        total = total + unique_day(i[1], possible_birthdays)
    if total != 0:
        return True
    else:
        return False