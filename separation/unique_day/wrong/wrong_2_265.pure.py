def unique_day(day, possible_birthdays):
    counter = 0
    for possible_birthday in possible_birthdays:
        if possible_birthday[1] == day:
            counter += 1
    if counter > 1:
        return False
    return True