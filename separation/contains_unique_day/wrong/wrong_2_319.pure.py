def contains_unique_day(month, possible_birthdays):
    days = ()
    for i in possible_birthdays:
        if month in i:
            days += (i[1],)
    for j in days:
        if unique_day(j, possible_birthdays):
            return True
    return False