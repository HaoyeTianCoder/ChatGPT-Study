def unique_day(date, possible_birthdays):
    count = 0
    for bday in possible_birthdays:
        if day == bday[1]:
            count += 1
    return count == 1