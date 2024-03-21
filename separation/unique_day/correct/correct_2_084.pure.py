def unique_day(day, possible_birthdays):
    count = 0
    for k in possible_birthdays:
        if k[1] == day:
            count = count + 1
        else:
            continue
    if count == 1:
        return True
    else:
        return False