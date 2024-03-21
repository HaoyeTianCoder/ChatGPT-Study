def contains_unique_day(month, possible_birthdays):
    month_tup = ()
    for tup in possible_birthdays:
        if month in tup:
            month_tup += (tup,)
    for tup in month_tup:
        if unique_day(tup[1],possible_birthdays):
            return True
    return False