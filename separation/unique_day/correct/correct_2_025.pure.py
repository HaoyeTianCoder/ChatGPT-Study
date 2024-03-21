def unique_day(day, possible_birthdays):
    counter = 0
    for birthday in possible_birthdays:
        counter += 1 if day == birthday[1] else 0
    return (counter == 1)