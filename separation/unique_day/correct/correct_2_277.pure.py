def unique_day(day, possible_birthdays):
    count = 0
    for i in possible_birthdays:
        if day == i[1]:
            count = count + 1
    if count == 1:
        return True
    else:
        return False