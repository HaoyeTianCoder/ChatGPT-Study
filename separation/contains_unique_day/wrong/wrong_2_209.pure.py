def contains_unique_day(month, possible_birthdays):
    tup = ()
    for i in possible_birthdays:
        if i[0] == month:
            tup += ((i),)
        else:
            continue
    for i in tup:
        if unique_day(i[1], possible_birthdays) == True:
            return True
    return False