def unique_day(day, possible_birthdays):
    result = 0
    for i in possible_birthdays:
        if day == i[1]:
            result = result + 1
        else:
            continue 
    if result == 1:
        return True
    else:
        return False