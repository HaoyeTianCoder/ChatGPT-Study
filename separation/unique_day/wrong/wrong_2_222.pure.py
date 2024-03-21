def unique_day(day, possible_birthdays):
    count = 0
    for date in possible_birthdays:
        if date[1] == day:
            count += 1
    return count == 1