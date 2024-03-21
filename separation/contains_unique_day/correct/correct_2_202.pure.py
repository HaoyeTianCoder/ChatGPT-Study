def contains_unique_day(month, possible_birthdays):
    new = ()
    for i in possible_birthdays:
        if i[0] == month:
            new = new + (i[1],)
    for i in new:
        if unique_day(i, possible_birthdays):
            return True
    return False