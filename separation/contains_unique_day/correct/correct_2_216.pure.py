def contains_unique_day(month, possible_birthdays):
    months = ()
    for i in possible_birthdays:
        if i[0] == month:
            months = months + (i,)
        else:
            continue
    for i in months:
        if unique_day(i[1], possible_birthdays) == True:
            return True
        else:
            continue
    return False