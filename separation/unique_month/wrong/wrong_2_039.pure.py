def unique_month(month, possible_birthdays):
    tup = ()
    for i in possible_birthdays:
        if i[0] == month:
            tup += (i[0],)
    if len(tup) == 1:
        return True
    else:
        return False