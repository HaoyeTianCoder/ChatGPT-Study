def unique_day(day, possible_birthdays):
    checker = []
    for bday in possible_birthdays:
        if day == bday[1] and day not in checker:
            checker.append(day)
        elif day == bday[1] and day in checker:
            return False
    return True