def contains_unique_day(month, possible_birthdays):
    month_day = ()
    for j in possible_birthdays:
        if j == possible_birthdays[0]:
            month_day = month_day + (j,)
    for t in month_day:
        return unique_day(t[1], month_day)