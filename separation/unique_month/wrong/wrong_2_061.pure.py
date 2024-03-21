def unique_month(month, possible_birthdays):
    months = tuple(filter(lambda x: x[0] == month, possible_birthdays))
    if len(months) <= 1:
        return True
    else:
        return False