def contains_unique_day(month, possible_birthdays):
    month_tup = ()
    for i in possible_birthdays:
        if month in i:
            month_tup = month_tup + possible_birthdays[i]
    return unique_day(day, month_tup)