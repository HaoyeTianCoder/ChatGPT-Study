def contains_unique_day(month, possible_birthdays):
    possible_days = ()
    for date in possible_birthdays:
        if month == date[0]:
            possible_days += (date[1],)
        else:
            continue
    for day in possible_days:
        if unique_day(day,possible_birthdays):
            return True
        else:
            continue
    return False