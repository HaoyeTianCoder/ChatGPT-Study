def contains_unique_day(month, possible_birthdays):
    wanted_month = ()
    for i in possible_birthdays:
        if i[0] == month:
            wanted_month += (i,)
    wanted_month_days = list(map(lambda x: x[1], wanted_month))
    unique_days = list(filter(lambda x: unique_day(x, possible_birthdays), wanted_month_days))
    return len(unique_days) > 0