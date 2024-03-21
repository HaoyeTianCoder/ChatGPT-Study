def contains_unique_day(month, possible_birthdays):
    filter_by_month = tuple( filter(lambda x: x[0] == month, possible_birthdays))
    for date in filter_by_month:
        if unique_day(date[1], possible_birthdays):
            return True
    return False