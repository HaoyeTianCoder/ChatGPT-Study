def unique_day(day, possible_birthdays):
    counter = 0
    for x in possible_birthdays:
        x_day = x[1]
        if day == x_day:
            counter += 1
        else:
            counter = counter
    if counter == 1:
        return True
    else:
        return False