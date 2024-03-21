def unique_day(day, possible_birthdays):
    for x in possible_birthdays:
        if day in x:
            return True
        else:
            return False