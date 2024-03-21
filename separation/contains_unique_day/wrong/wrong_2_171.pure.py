def contains_unique_day(month, possible_birthdays):
    months = tuple(filter(lambda x: x[0] == month, possible_birthdays))
    result = tuple(filter(lambda y: unique_day(y[1], possible_birthdays), months))
    if len(result) == 1:
        return True
    else:
        return False