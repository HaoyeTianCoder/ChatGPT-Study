def unique_month(month, possible_birthdays):
    tester = 0
    for i in possible_birthdays:
        if date == i[0]:
            if tester:
                return False
            else:
                tester = 1
    return tester