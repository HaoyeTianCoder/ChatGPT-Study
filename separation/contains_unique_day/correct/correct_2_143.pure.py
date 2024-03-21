def contains_unique_day(month, possible_birthdays):
    count = 0
    matchmonth = ()
    for i in possible_birthdays:
        if month == i[0]:
            matchmonth += (i,)
    for i in matchmonth:
        if unique_day(i[1], possible_birthdays):
            return True
    return False