def unique_day(date, possible_birthdays):
    total= 0
    for i in possible_birthdays:
        if date == i[1]:
            total= total + 1
    return total == 1