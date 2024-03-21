def contains_unique_day(month, possible_birthdays):
    dates =()
    for birthdays in possible_birthdays:
        if unique_day(birthdays[1], possible_birthdays):
            dates += (birthdays[0],)
    for days in dates:
        if month in dates:
            return True
        break
    return False