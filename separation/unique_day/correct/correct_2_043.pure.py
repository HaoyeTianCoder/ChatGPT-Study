def unique_day(date, possible_birthdays):
    num = 0
    for birthday in possible_birthdays:
        if date == birthday[1]:
            num += 1
    return num == 1