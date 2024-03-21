def contains_unique_day(month, possible_birthdays):
    counter = 0
    dummy = ()
    indicator = ()
    for i in possible_birthdays:
        if month == i[0]:
            dummy += (i,)
    for i in dummy:
        indicator += (unique_day(i[1],possible_birthdays),)
    if True not in indicator:
        return False
    else:
        return True