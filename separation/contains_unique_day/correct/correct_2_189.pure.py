def contains_unique_day(month, possible_birthdays):
    days_in_month = map(lambda x: x[1] if x[0] == month else (), possible_birthdays)
    check = map(lambda x: unique_day(x, possible_birthdays), days_in_month)
    return True in check