def unique_day(day, possible_birthdays):
    count = 0
    for possible_birthday in possible_birthdays:
        if day == possible_birthday[1]:
            count += 1
    return count == 1