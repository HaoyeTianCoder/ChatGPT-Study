def unique_day(date, possible_birthdays):
    counter = 0
    for bday in possible_birthdays:
        if date == bday[1]:
            counter += 1
    if counter > 1:
        return False
    return True