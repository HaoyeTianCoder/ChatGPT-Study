def contains_unique_day(month, possible_birthdays):
    days = ()
    for i in possible_birthdays:
        if month == i[0]:
            days += (i[1],)
    for i in days:
        if unique_date(i, possible_birthdays):
            return True
        else:
            return false