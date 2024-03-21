def contains_unique_day(month, possible_birthdays):
    days_in_month = ()
    for bday in possible_birthdays:
        if month == bday[0]:
            days_in_month += (bday[1],)
    for day in days_in_month:
        if unique_day(day, possible_birthdays) == True:
            return True
    return False