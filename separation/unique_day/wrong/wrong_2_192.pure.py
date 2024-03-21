def unique_day(day, possible_birthdays):
    i=0
    for birthday in possible_birthdays:
        if day == birthday[1]:
            i+=1
            if i == 2:
                return False
    return True