def unique_day(day, possible_birthdays):
    count = 0
    for x in possible_birthdays:
        if day in x:
            count += 1
    return count == 1