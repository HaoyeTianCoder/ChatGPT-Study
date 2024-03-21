def unique_month(month, possible_birthdays):
    total = ()
    for i in possible_birthdays:
        total += (i[0],)
    if total.count(month) > 1: 
        return False
    else:
        return True