def unique_day(day, possible_birthdays):
    get_possible_days = map(lambda bdays:bdays[1],possible_birthdays)
    count = 0
    for days in get_possible_days:
        if days == day:
            count = count + 1
    if count == 1:
        return True
    else:
        return False