def unique_month(month, possible_birthdays):
    possible_months = tuple(map(lambda x: x[0], possible_birthdays))
    if possible_months.count(month) == 1:
        return True
    else:
        return False