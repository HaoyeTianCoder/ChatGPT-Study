def contains_unique_day(month, possible_birthdays):
    birthdays = ()
    for i in possible_birthdays:
        if month in i:
            birthdays += (i,)
    for i in birthdays:
        if not unique_day(i[1], possible_birthdays):
            result = False
        else:
            result = True
            break
    return result