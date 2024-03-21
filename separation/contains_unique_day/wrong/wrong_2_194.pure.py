def contains_unique_day(month, possible_birthdays):
    y = ()
    for i in possible_birthdays:
        if i[0] == month:
            y = y + (i, )
    for a in y:
        if unique_day(a[1], possible_birthdays):
            return True
    return False