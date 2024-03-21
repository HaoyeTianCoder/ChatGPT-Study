def unique_day(day, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if day in i:
            counter += 1
    return counter == 1