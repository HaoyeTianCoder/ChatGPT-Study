def unique_day(day, possible_birthdays):
    count = 0
    for element in possible_birthdays:
        if element[1] == day:
            count += 1
    if count != 1:
        return False
    return True