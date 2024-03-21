def unique_day(date, possible_birthdays):
    count = 0
    for birthday in possible_birthdays:
        if birthday[1] == date:
            count += 1
    return count == 1