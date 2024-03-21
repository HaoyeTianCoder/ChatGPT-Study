def unique_day(date, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if i[1] == date:
            counter += 1
    if counter > 1:
        return False
    return True