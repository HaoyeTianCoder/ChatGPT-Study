def unique_month(month, possible_birthdays):
    if (tuple(map(lambda x: x[0], possible_birthdays))).count(month) == 1:
        return True
    return False