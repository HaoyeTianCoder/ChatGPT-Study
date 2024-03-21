def unique_day(day, possible_birthdays):
    counter = 0
    for elem in possible_birthdays:
        birthday = elem[1]
        if birthday == day:
            counter += 1
    if counter == 1:
        return True
    else:
        return False