def contains_unique_day(month, possible_birthdays):
    more_possible_dates = filter(lambda date: date[0] == month, possible_birthdays)
    for date in more_possible_dates:
        if unique_day(date[1], possible_birthdays):
            return True
    return False