def contains_unique_day(month, possible_birthdays):
    filter_month = tuple(filter(lambda x: x[0] == month, possible_birthdays))
    for day in filter_month:
        if unique_day(day[1], possible_birthdays):
            return True
    return False