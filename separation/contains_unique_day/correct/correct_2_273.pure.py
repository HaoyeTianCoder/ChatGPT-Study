def contains_unique_day(month, possible_birthdays):
    special_days = tuple(filter((
        lambda x: unique_day(x[1], possible_birthdays)),
                                possible_birthdays))
    for i in special_days:
        if i[0] == month:
            return True
    return False