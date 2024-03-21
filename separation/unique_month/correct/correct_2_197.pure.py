def unique_month(month, possible_birthdays):
    result = 0
    for i in range(len(possible_birthdays)):
        if month in possible_birthdays[i]:
            result += 1
    if result == 1:
        return True
    else:
        return False