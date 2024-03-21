def contains_unique_day(month, possible_birthdays):
    unique_day_tuple = tuple(filter(lambda x: unique_day(x[1],possible_birthdays),possible_birthdays))
    for i in unique_day_tuple:
        if i[0] == month:
            return True
    return False