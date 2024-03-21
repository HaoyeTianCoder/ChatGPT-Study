def unique_day(day, possible_birthdays):
    days = tuple(filter(lambda x: x[1] == day, possible_birthdays))
    if len(days) <= 1:
        return True
    else:
        return False