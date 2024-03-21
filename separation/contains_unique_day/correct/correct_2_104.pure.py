def contains_unique_day(month, possible_birthdays):
    dates = ()
    for z in possible_birthdays:
        if unique_day(z[1], possible_birthdays):
            dates += (z,)
        else:
            continue
    for i in dates:
        if i[0] == month:
            return True
    else:
        return False