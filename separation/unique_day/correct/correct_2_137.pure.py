def unique_day(day, possible_birthdays):
    a  = 0
    for date in possible_birthdays:
        cb = date[1]
        if day == cb:
            a+= 1
        else:
            continue
    if a==1:
        return True
    else:
        return False