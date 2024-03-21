def unique_day(day, possible_birthdays):
    counter = 0
    for birthday in possible_birthdays:
        birthday_day = birthday[1]
        if day == birthday_day:
            counter += 1
    if counter == 1:
        return True
    else:
        return False