def unique_month(month, possible_birthdays):
    months = ()
    unique = ()
    for i in possible_birthdays:
        months += (i[0],)
    for i in months:
        if i == month:
            unique += (i,)
        else:
            continue
    if len(unique) == 1:
        return True
    else:
        return False