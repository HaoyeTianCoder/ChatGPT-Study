def unique_day(day, possible_birthdays):
    count = 0
    for i in possible_birthdays:
        if i[1] == day:
            count = count + 1
    if count == 1:
        return True
    else:
        return False