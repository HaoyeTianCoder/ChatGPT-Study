def unique_day(day, possible_birthdays):
    result = 0
    for birthdays in possible_birthdays:
        if birthdays[1] == day:
            result = result + 1
    if result == 1:
        return True
    else:
        return False