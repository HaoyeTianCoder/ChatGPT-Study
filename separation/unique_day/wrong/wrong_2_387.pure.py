def unique_day(date, possible_birthdays):
    counter = 0
    for birthdate in possible_birthdays:
        if str(date) == birthdate[1]:
            counter += 1
    if counter > 1:
        return False
    else:
        return True