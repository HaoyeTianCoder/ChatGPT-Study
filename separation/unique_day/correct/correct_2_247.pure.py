def unique_day(date, possible_birthdays):
    result = 0
    for n in possible_birthdays:
        if n[1] == date:
            result = result + 1
    if result != 1:
        return False
    else:
        return True