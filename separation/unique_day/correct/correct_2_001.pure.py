def unique_day(day, possible_birthdays):
    all_days = ()
    for i in possible_birthdays:
        all_days += (i[1],)
    return all_days.count(day) == 1