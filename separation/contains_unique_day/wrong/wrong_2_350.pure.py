def contains_unique_day(month, possible_birthdays):
    tuppy = ()
    for x in possible_birthdays:
        if unique_day(x[1], possible_birthdays):
            tuppy += (x, )
    for y in tuppy:
        if y[0] == month:
            return True
    return False