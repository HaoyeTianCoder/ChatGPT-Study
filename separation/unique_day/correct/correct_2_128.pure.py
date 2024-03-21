def unique_day(day, possible_birthdays):
    counter = 0
    for birthday in possible_birthdays:
        if day == birthday[1]:
            counter += 1            
    return counter == 1