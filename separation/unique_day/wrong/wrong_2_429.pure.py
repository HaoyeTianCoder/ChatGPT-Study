def unique_day(day, possible_birthdays):
    all_days = ()
    repeat_days =()
    for date in possible_birthdays:
        if date[1] not in all_days:
            all_days += (date[1],)
        else:
            repeat_days += (date[1],)
    return day not in repeat_days   