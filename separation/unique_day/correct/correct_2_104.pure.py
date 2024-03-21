def unique_day(date, possible_birthdays):
    dates = ()
    for d in possible_birthdays:
        dates += (d[1],)
    if dates.count(date) == 1:
        return True
    else:
        return False