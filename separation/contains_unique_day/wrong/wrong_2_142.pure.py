def contains_unique_day(month, possible_birthdays):
    for x in days(month, possible_birthdays):
        if unique_day(x, possible_birthdays):
            return True
        else:
            return False