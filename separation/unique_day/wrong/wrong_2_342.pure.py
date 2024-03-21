def unique_day(date, possible_birthdays):
    count = 0
    for birthday in possible_birthdays:
        if date == birthday[1]:
            count = count + 1
    if count>1:
        return False
    else:
        return True    