def contains_unique_day(month, possible_birthdays):
    for x in range(len(days(month, possible_birthdays))):
        if unique_day(days(month, possible_birthdays)[x], possible_birthdays):
            return True
        else:
            return False