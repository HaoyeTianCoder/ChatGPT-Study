def unique_day(day, possible_birthdays):
    counter = 0
    for item in possible_birthdays:
        if item[1] == day:
            counter = counter + 1
    if counter !=1:
        return False
    return True