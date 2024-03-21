def contains_unique_day(month, possible_birthdays):
    unique_days = tuple(filter(lambda x: unique_day(x[1], possible_birthdays), possible_birthdays))
    for birthday in unique_days:
        if birthday[0] == month:
            return True
    return False