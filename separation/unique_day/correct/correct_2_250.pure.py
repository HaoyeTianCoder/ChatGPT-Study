def unique_day(day, possible_birthdays):
    data=()
    for birthday in possible_birthdays:
        if day == birthday[1]:
            data += (birthday,)
    if len(data)==1:
        return True
    else:
        return False