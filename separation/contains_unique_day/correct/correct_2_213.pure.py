def contains_unique_day(month, possible_birthdays):
    choose_month = ()
    uniqueday_in_month = ()
    for i in possible_birthdays:
        if i[0] == month:
            choose_month += (i,)
        else:
            continue
    for i in choose_month:
        if unique_day(i[1], possible_birthdays) == True:
            return True
    return False