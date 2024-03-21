def unique_day(date, possible_birthdays):
    result = 0
    for i in possible_birthdays:
        if i[1] == day:
            result += 1
        elif i[1] != day:
            result += 0
    if result == 1:
        return True
    else:
        return False