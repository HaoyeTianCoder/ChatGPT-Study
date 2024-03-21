def unique_day(day, possible_birthdays):
    appearance = 0
    for i in possible_birthdays:
        if i[1] == day:
            appearance += 1
    if appearance == 1:
        return True
    return False