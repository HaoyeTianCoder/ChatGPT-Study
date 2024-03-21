def unique_day(day, possible_birthdays):
    x = ()
    y = ()
    for i in possible_birthdays:
        x += (i[1],)
    for i in x:
        if i == day:
            y += (i,)
        else:
            continue
    if len(y) == 1:
        return True
    else:
        return False