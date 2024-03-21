def unique_month(month, possible_birthdays):
    for i in range (len(possible_birthdays)):
        if possible_birthdays[i][0] == month:
            for j in range (i + 1, len(possible_birthdays)):
                if possible_birthdays[j][0] == month:
                    return False
    return True