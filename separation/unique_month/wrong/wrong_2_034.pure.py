def unique_month(month, possible_birthdays):
    tpl = ()
    for j in possible_birthdays:
        tpl += (j[0],)
    if tpl.count(month) > 1:
        return False
    return True    