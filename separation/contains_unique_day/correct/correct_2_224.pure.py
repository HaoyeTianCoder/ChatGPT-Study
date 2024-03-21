def contains_unique_day(month, possible_birthdays):
    bag = ()
    for months in possible_birthdays:
        if months[0] == month:
            bag += ((months[1]),)
    for days in bag:
        if unique_day(days,possible_birthdays):
            return True
    else:
        return False