def unique_day(day, possible_birthdays):
    a = 0
    for item in possible_birthdays:
        for i in item:
            if i == day:
                a += 1
    if a == 1:
        return True
    else:
        return False