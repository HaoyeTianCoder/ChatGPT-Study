def unique_day(day, possible_birthdays):
    count = 0
    for possible_dates in possible_birthdays:
        if possible_dates[1] == day:
            count += 1
    if count != 1:
        return False
    return True