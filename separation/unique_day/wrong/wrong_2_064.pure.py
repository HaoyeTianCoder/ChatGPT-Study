def unique_day(day, possible_birthdays):
    unique = False
    for i in possible_birthdays:
        if day == i[1]:
            if unique:
                return False
            else:
                unique = True
    return True