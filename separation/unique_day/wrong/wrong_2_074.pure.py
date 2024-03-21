def unique_day(date, possible_birthdays):
    no_of_days = 0
    for i in possible_birthdays:
        if i[1] == day:
            no_of_days += 1
    if no_of_days != 1:
        return False
    return True