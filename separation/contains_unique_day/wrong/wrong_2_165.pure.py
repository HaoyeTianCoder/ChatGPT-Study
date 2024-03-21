def contains_unique_day(month, possible_birthdays):
    for x in range(len(days(month, possible_birthdays))):
        if unique_day(x, possible_birthdays):
            return True
        elif unique_day(days(month, possible_birthdays)[-1], possible_birthdays):
            return False