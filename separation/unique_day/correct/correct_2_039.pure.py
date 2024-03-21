def unique_day(day, possible_birthdays):
    day_count = 0
    for birthday in possible_birthdays:
        if birthday[1] == day:
            day_count = day_count + 1
        if day_count > 1:
            break
    if day_count == 1:
        return True
    else:
        return False