def unique_month(month, possible_birthdays):
    return tuple(map(lambda x: x[0], possible_birthdays)).count(month) == 1