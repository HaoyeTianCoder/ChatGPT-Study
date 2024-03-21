def contains_unique_day(month, possible_birthdays):
    possible_birthdays_in_month = tuple(filter(lambda x: x[0] == month, possible_birthdays))
    for i in possible_birthdays_in_month:
        if unique_day(i[1], possible_birthdays):
            return True
    else:
        return False