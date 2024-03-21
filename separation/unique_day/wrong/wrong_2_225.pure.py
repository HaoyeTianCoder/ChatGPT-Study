def unique_day(day, possible_birthdays):
    count = 0
    for i in possible_birthdays:
        birthday = i[1]
        if day == birthday:
            count = count + 1
        else:
            count = count
    if count > 1:
        return False
    elif count <= 1:
        return True