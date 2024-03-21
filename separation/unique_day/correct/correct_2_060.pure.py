def unique_day(day, possible_birthdays):
    total_day = 0
    for birthday in possible_birthdays:
        if birthday[1] == day:
            total_day += 1
    if total_day == 1:
        return True
    else:
        return False