def unique_day(day, possible_birthdays):
    i = 0
    for days in possible_birthdays:
        if int(day) == int(days[1]):
            i += 1
        else:
            i = i
    if counter == 1:
        return True
    else:
        return False