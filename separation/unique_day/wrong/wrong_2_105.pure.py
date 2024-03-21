def unique_day(date, possible_birthdays):
    count = 0
    for i in possible_birthdays:
        if i[1] == date:
            count += 1
    return count
    if count == 1:
        return True
    else:
        return False