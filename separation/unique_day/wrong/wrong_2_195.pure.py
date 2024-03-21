def unique_day(date, possible_birthdays):
    counter = 0
    for j in possible_birthdays:
        if day == j[1]:
            counter += 1
    if counter != 1:
        return False
    else:
        return True