def unique_day(day, possible_birthdays):
    unique_day_counter = 0
    for i in possible_birthdays:
        if day == i[1]:
            unique_day_counter += 1
    if unique_day_counter != 1:
        return False
    return True