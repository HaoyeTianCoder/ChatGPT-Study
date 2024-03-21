def unique_day(day, possible_birthdays):
    result = 0
    for bday in possible_birthdays:
        if bday[1] == day:
            result += 1
    return result == 1