def unique_month(month, possible_birthdays):
    i, times = 0, 0
    while i < len(possible_birthdays):
        if possible_birthdays[i][0] == month:
            times += 1
        i += 1
    if times == 1:
        return True
    else:
        return False