def unique_day(day, possible_birthdays):
    day_count = 0
    for i in possible_birthdays:
        if day in i:
            day_count += 1
        if day_count > 1:
            return False
    if day_count == 0:
        return False   
    return True