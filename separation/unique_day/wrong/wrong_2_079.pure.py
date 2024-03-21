def unique_day(day, possible_birthdays):
    total = 0
    for i in possible_birthdays:
        if i[1] == day:
            total += 1
    if total > 1:
        return False
    return True