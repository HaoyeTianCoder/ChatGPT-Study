def unique_month(month, possible_birthdays):
    bag = ()
    for date in possible_birthdays:
        if date[0] == month:
            bag += (date[0],)
    if len(bag) >= 2:
        return False
    return True