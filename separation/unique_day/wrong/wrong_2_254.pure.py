def unique_day(date, possible_birthdays):
    counter = 0
    for birthday in possible_birthdays:
        if birthday[1]== day:
            counter = counter + 1
    if counter <= 1:
        return True
    else:
        return False