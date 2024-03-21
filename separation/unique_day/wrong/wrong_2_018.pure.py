def unique_day(day, possible_birthdays):
    count_day = 0
    for birthday in possible_birthdays:
        if day == birthday[1]:
            if count_day == 0: count_day += 1
            else: return False
    return True