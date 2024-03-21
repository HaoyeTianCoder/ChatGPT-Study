def unique_day(day, possible_birthdays):
    unique = 0
    for i in possible_birthdays:
        if i[1] == day:
            unique += 1
    if unique > 1:
        return False
    return True