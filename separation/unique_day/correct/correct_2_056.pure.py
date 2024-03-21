def unique_day(day, possible_birthdays):
    freq=0
    for birthday in possible_birthdays:
        if birthday[1]==day:
            freq=freq+1
        else:
            continue
    if freq==1:
        return True
    else:
        return False