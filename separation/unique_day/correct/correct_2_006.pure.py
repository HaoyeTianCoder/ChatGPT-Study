def unique_day(day, possible_birthdays):
    possible_days = tuple(map(lambda x: x[1], possible_birthdays))
    if possible_days.count(day) == 1:
        return True
    else:
        return False