def contains_unique_day(month, possible_birthdays):
    month_day = ()
    for j in possible_birthdays:
        if month == j[0]:
            month_day = month_day + (j,)
    for t in month_day:
        if unique_day(t[1], possible_birthdays) == True:
            return True
    return False