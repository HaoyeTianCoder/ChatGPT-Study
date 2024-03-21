def contains_unique_day(month, possible_birthdays):
    tup = ()
    for date in possible_birthdays:
        if date[0] == month:
            tup += (date,)
    for bday in tup:
        if unique_day(bday[1], possible_birthdays):
            return True
    return False