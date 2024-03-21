def unique_month(month, possible_birthdays):
    month = 0
    for i in range(len(possible_birthdays)):
        if possible_birthdays[i][0] == month:
            day = day + 1
    if days == 1:
        return True
    else:
        return False 