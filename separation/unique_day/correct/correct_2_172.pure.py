def unique_day(day, possible_birthdays):
    a=0
    for birthday in possible_birthdays:
        if day == birthday[1]:
            a = a + 1
    if a == 1:
        return True
    else:
        return False