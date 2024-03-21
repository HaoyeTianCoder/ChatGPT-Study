def unique_day(day, possible_birthdays):
    days = ()
    for elem in possible_birthdays:
        days += (elem[1],)
    times = days.count(day)
    if times == 1:
        return True
    else:
        return False