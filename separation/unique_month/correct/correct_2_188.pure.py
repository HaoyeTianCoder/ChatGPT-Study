def unique_month(month, possible_birthdays):
    n = len(possible_birthdays)
    result = 0
    for counter in range(n):
        if month == possible_birthdays[counter][0]:
            result = result + 1
    return result == 1