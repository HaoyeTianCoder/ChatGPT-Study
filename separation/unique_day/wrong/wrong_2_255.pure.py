def unique_day(day, possible_birthdays):
    count = 0
    for element in possible_birthdays:
        if day == element[1]:
            count += 1
    if count > 1:
        return False
    else:
        return True