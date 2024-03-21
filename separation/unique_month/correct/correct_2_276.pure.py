def unique_month(month, possible_birthdays):
    x = ()
    y = ()
    for i in possible_birthdays:
        x += (i[0],)
    for i in x:
        if i == month:
            y += (i,)
        else:
            continue
    if len(y) == 1:
        return True
    else:
        return False