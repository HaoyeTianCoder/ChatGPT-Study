def contains_unique_day(month, possible_birthdays):
    n = len(possible_birthdays)
    for counter in range(n):
        if month == possible_birthdays[counter][0]:
            if unique_day(possible_birthdays[counter][1], possible_birthdays) == True:
                return True
    return False