def unique_month(month, possible_birthdays):
    count = tuple(filter(lambda x: x[0] == month, possible_birthdays))
    if len(count) == 1:
        return True
    return False