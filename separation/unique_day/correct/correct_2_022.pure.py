def unique_day(day, possible_birthdays):
    count_day = 0
    for i in possible_birthdays:
        if i[1] == day:
            count_day += 1
    if count_day == 1:
        return True
    return False