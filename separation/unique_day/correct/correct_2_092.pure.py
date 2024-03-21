def unique_day(day, possible_birthdays):
    if (tuple(map(lambda x: x[1], possible_birthdays))).count(day) == 1:
        return True
    return False