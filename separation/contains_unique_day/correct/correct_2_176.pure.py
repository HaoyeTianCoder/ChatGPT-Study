def contains_unique_day(month, possible_birthdays):
    selected_month = ()
    unique = ()
    for i in possible_birthdays:
        if i[0] == month:
            selected_month += (i,)
        else:
            continue
    for i in selected_month:
        if unique_day(i[1], possible_birthdays) == True:
            return True
    return False