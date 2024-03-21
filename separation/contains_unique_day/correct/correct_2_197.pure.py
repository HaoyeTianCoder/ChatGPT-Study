def contains_unique_day(month, possible_birthdays):
    days = ()
    for i in possible_birthdays:
        if i[0] == month:
            days += (i[1],)
    for i in days:
        if unique_day(i, possible_birthdays):
            return True
    return False