def unique_month(month, possible_birthdays):
    check_month = tuple(filter(lambda x: x[0] == month, possible_birthdays))
    if len(check_month) == 1:
        return True
    return False