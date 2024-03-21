def unique_day(day, possible_birthdays):
    check_day = tuple(filter(lambda x: x[1] == day, possible_birthdays))
    if len(check_day) == 1:
        return True
    return False