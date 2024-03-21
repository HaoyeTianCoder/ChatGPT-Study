def unique_month(month, possible_birthdays):
    uniquemonth = ()
    months = ()
    for i in possible_birthdays:
        months += (i[0],)
    for i in months:
        if i == month:
            uniquemonth += (i,)
        else:
            continue
    if len(uniquemonth) == 1:
        return True
    else:
        return False