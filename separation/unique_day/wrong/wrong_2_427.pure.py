def unique_day(date, possible_birthdays):
    only_date = ()
    for i in possible_birthdays:
        if date in i:
            only_date = only_date + (i,)
    if len(only_date) == 1:
        return True
    else:
        return False