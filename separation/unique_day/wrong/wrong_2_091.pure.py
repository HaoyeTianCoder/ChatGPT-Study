def unique_day(day, possible_birthdays):
    days = ()
    for all_days in possible_birthdays:
        days = days + (all_days[1],)
        i = 0
        for all_days in days:
            if all_days == day:
                i = i+1
    if i == 1:
        return True
    else:
        return False