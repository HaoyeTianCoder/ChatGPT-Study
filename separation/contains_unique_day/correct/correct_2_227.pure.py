def contains_unique_day(month, possible_birthdays):
    a = filter(lambda birth_month: month == birth_month[0], possible_birthdays)
    for i in a:
        if unique_day(i[1],possible_birthdays):
            return True
    return False 