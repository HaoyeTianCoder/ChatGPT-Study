def unique_month(month, possible_birthdays):
    a = 0
    for date in possible_birthdays:
        lj = date[0]
        if month == lj:
           a+= 1
        else:
            continue
    if a == 1:
        return True
    else:
        return False