def contains_unique_day(month, possible_birthdays):
    x = ()
    y = ()
    for i in possible_birthdays:
        if i[0] == month:
            x += (i,)
        else:
            continue
    for i in x:
        if unique_day(i[1], possible_birthdays) == True:
            return True
    return False