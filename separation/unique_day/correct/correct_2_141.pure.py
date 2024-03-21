def unique_day(day, possible_birthdays):
    count = tuple(filter(lambda x: x[1] == day, possible_birthdays))
    if len(count) == 1:
        return True
    return False