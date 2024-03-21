def unique_day(day, possible_birthdays):
    return tuple(map(lambda x: x[1], possible_birthdays)).count(day) == 1