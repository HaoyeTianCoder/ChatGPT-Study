def unique_day(day, possible_birthdays):
    count = 0
    for birthday in possible_birthdays:
        if birthday[1] == day:
            count = count + 1
            if count > 1:
                return False
    return True