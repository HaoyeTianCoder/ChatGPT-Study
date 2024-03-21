def contains_unique_day(month, possible_birthdays):
    for x in range(len(days(month, possible_birthdays))):
        if unique_day(x, possible_birthdays) == False:
            return True
        else:
            return False