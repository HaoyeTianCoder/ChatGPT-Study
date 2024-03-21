def unique_day(day, possible_birthdays):
    counter = 0
    for x in possible_birthdays:
        if day == x[1]:
            counter += 1
    if counter == 1:
        return True
    else:
        return False