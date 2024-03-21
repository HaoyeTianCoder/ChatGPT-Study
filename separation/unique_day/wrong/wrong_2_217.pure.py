def unique_day(date, possible_birthdays):
    j = 0
    for i in possible_birthdays:
        if day == i[2]:
            j = j+1
        else:
            j = j
    if j == 1:
        return True
    else:
        return False