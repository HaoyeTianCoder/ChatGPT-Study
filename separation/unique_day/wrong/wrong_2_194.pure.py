def unique_day(day, possible_birthdays):
    x = 1
    for i in possible_birthdays:
        if day == i[1]:
            x = x + 1
        else:
            x = x
    if x > 2:
        return False
    else:
        return True