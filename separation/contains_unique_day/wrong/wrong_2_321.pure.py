def contains_unique_day(month, possible_birthdays):
    unique_days = ()
    month_birthdays = ()
    for day in range(0, 32):
        if unique_day(str(day), possible_birthdays) == True:
            unique_days = unique_days + (day,)
    for birthday in possible_birthdays:
        if birthday[0] == month:
            month_birthdays = month_birthdays + (birthday,)
    for dates in month_birthdays:
        if int(dates[1]) in unique_days:
            return True
    else:
        return False