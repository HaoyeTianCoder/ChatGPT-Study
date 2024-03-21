def unique_day(date, possible_birthdays):
    tpl = ()
    for i in possible_birthdays:
        tpl += (i[1],)
    if tpl.count(date) > 1:
        return False
    return True    