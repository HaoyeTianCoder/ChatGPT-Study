def unique_day(day, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if day in i:
            counter += 1
    if counter == 1:
        return True
    else:
        return False