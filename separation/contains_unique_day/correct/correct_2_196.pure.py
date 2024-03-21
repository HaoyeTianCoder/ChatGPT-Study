def contains_unique_day(month, possible_birthdays):
    mth = tuple(filter(lambda bd: month == bd[0], possible_birthdays))
    for i in mth:
        if unique_day(i[1], possible_birthdays):
            return True
    return False