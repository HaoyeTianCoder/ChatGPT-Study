def unique_day(day, possible_birthdays):
    if len(tuple(filter(
        lambda x : x[1] == day, possible_birthdays))) == 1:
        return True
    return False