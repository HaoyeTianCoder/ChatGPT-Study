def contains_unique_day(month, possible_birthdays):
    date_day = ()
    for date in possible_birthdays:
        if date[0] == month:
            date_day += (date[1],)
    for check in date_day: 
        check_day = tuple(filter(lambda x: x[1] == check, possible_birthdays))
        if len(check_day) == 1:
            return True
    return False