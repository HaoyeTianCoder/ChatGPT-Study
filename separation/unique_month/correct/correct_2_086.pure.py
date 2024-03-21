def unique_month(month, possible_birthdays):
    value = 0
    for i in range(0, len(possible_birthdays)):
        if (month == possible_birthdays[i][0]):
            value += 1
    if (value > 1) or (value == 0):
        return False
    else:
        return True