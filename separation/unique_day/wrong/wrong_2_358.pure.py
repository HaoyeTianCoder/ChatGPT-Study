def unique_day(day, possible_birthdays):
    bag = ()
    for date in possible_birthdays:
        if date[1] == day:
            bag += (date[1],)
    if len(bag) >= 2:
        return False
    return True