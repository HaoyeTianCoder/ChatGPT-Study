def unique_month(month, possible_birthdays):
    if len(tuple(filter(
        lambda x : x[0] == month, possible_birthdays))) == 1:
        return True
    return False