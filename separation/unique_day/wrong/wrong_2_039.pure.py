def unique_day(day, possible_birthdays):
    tup = ()
    for i in possible_birthdays:
        if i[1] == day:
            tup += (i[1],)
    if len(tup) == 1:
        return True
    elif len(tup) > 1:
        return False
    elif len(tup) == 0:
        return None