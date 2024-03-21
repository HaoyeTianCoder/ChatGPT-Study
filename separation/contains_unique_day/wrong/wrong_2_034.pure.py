def contains_unique_day(month, possible_birthdays):
    tpl = ()
    for k in possible_birthdays:
        if k[0] == month:
            tpl += (k[1],)
    for l in tpl:
        if unique_day(l, possible_birthdays) == True:
            return True
    return False        