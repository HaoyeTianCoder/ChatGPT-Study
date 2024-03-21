def contains_unique_day(month, possible_birthdays):
    counter = 0
    filtered_dates = ()
    for dates in possible_birthdays:
        if month in dates:
            filtered_dates += (dates,)
    for date in filtered_dates:
        if unique_day(date[1], possible_birthdays):
            return True
    return False