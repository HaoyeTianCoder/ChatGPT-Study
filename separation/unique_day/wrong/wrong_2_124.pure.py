def unique_day(date, possible_birthdays):
    tester = 0
    for i in possible_birthdays:
        if date == i[1]:
            if tester:
                return False
            else:
                tester = 1
    return tester