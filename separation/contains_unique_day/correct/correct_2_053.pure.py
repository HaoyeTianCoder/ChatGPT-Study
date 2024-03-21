def contains_unique_day(month, possible_birthdays):
    days_in_month = ()
    for i in possible_birthdays:
        if month in i:
            days_in_month += (i[1],)
    for i in days_in_month:
        if unique_day(i, possible_birthdays):
            return True
    return False