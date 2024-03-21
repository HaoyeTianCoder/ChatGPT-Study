def unique_month(month, possible_birthdays):
    count, result = 0, 0
    for count in range(0, len(possible_birthdays)):
        if month == possible_birthdays[count][0]:
            result = result + 1
        else:
            continue
    if result == 1:
        return True
    else:
        return False